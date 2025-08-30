from typing import Dict, Any, List, Tuple
from pydantic import BaseModel, Field
from loguru import logger
from config.llm_client import get_llm
import concurrent.futures

INSTRUCTION: str = """Convert the given mainframe BMS screen into a responsive, interactive HTML form, maintaining the structure and functionality of the screen while providing detailed labels and placeholders to ensure usability.

# Requirements:
1. Translate all visible fields and elements into corresponding HTML form components (e.g., text inputs, radio buttons, dropdowns, etc.).
2. Preserve the logical grouping and hierarchy of fields.
3. Include field labels for clarity and placeholders reflecting the example data.
4. Utilize responsive design principles for accessibility and compatibility across devices.
5. Map terminal function keys to action buttons, e.g., ENTER = Continue, F3 = Back, as appropriate for a web interface.
6. Ensure that fields requiring specific data formats (e.g., dates, numerical values) have appropriate HTML attributes (`type`, `pattern`, etc.).
7. Render any validation or constraints evident from the BMS screen (e.g., date formats, numerical constraints) using appropriate HTML attributes or comments.
8. Include a simple, clean CSS style for the form, focusing on readability and usability.
9. Ensure that the layout of the HTML form is visually similar to the original BMS screen. 
10. Do not enter new line that are displayed on the same line in the BMS screen.

# Output Format:
Provide the output as pure HTML, including comments for complex mappings or areas needing clarification. Do not use any additional frameworks or libraries unless explicitly stated. HTML code should be as clean and minimal as possible while being semantically correct. Use placeholders to represent content where necessary.

# Example Output:

**Input (BMS Screen Example)**:
```
Tran:               XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy  
Prog:               XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss  
                                                                                
                             Add Transaction                                    
                                                                                
     Enter Acct #:  XXXXXXXXXXX     (or)     Card #:  XXXXXXXXXXXXXXXX          
                                                                                
     ------------------------------------------------
               -----     
                                                                                
     Type CD: XX      Category CD: XXXX      Source: XXXXXXXXXX                 
                                                                                
     Description: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  
                                                                                
     Amount: XXXXXXXXXXXX     Orig Date: XXXXXXXXXX     Proc Date: XXXXXXXXXX   
            (-99999999.99)              (YYYY-MM-DD)              (YYYY-MM-DD)  
     Merchant ID: XXXXXXXXX     Merchant Name: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   
                                                                                
     Merchant City: XXXXXXXXXXXXXXXXXXXXXXXXX       Merchant Zip: XXXXXXXXXX    
                                                                                
                                                                                
     You are about to add this transaction. Please c-
       X  (Y/N)          
                                                                                
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  
ENTER=Continue  F3=Back  F4=Clear  F5=Copy Last-
```

**Output (HTML Example)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Add Transaction</title>
  <style>
    body {{
      font-family: 'Inter', sans-serif;
      background-color: #eef2f7;
      color: #333;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
    }}
    .container {{
      background-color: #ffffff;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
      max-width: 800px;
      width: 100%;
      box-sizing: border-box;
    }}
    .form-group {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 20px;
      margin-bottom: 20px;
    }}
    input[type="text"],
    input[type="date"],
    input[type="time"],
    input[type="number"] {{
      padding: 12px;
      border: 1px solid #ddd;
      border-radius: 8px;
      background-color: #fafafa;
      outline: none;
      transition: border-color 0.2s;
    }}
    input[type="text"]:focus,
    input[type="date"]:focus,
    input[type="time"]:focus,
    input[type="number"]:focus {{
      border-color: #4a90e2;
      box-shadow: 0 0 8px rgba(74, 144, 226, 0.2);
    }}
    input::placeholder {{
      color: #aaa;
    }}
    h2 {{
      text-align: center;
      margin-bottom: 25px;
      color: #333;
    }}
    button {{
      padding: 12px 20px;
      background-color: #4a90e2;
      border: none;
      color: white;
      cursor: pointer;
      border-radius: 6px;
      transition: background-color 0.3s ease;
    }}
    button:hover {{
      background-color: #357abd;
    }}
    .button-group {{
      text-align: center;
      margin-top: 25px;
    }}
    .confirm-field {{
      text-align: center;
      margin-top: 25px;
      font-weight: 500;
    }}
    label {{
      font-weight: 600;
    }}
  </style>
</head>
<body>
  <div class="container">
    <h2>Add Transaction</h2>

    <div class="form-group">
      <input type="text" placeholder="Transaction">
      <input type="date">
      <input type="text" placeholder="Program">
      <input type="time">
    </div>

    <div class="form-group">
      <input type="text" placeholder="Acct # (max 11)" maxlength="11">
      <input type="text" placeholder="Card #">
    </div>

    <div class="form-group">
      <input type="text" placeholder="Type CD (2 chars)" maxlength="2">
      <input type="text" placeholder="Category CD (4 chars)" maxlength="4">
      <input type="text" placeholder="Source">
    </div>

    <div class="form-group">
      <input type="text" placeholder="Description">
    </div>

    <div class="form-group">
      <input type="number" placeholder="Amount" step="0.01">
    </div>

    <div class="form-group">
      <input type="text" placeholder="Merchant ID">
      <input type="text" placeholder="Merchant Name">
    </div>

    <div class="form-group">
      <input type="text" placeholder="Merchant City">
      <input type="text" placeholder="Merchant Zip">
    </div>

    <div class="confirm-field">
      <label>Confirm Transaction (Y/N):</label>
      <input type="text" placeholder="Y/N" maxlength="1" style="width:60px; text-align:center;">
    </div>

    <div class="button-group">
      <button type="button">Continue (ENTER)</button>
      <button type="button">Back (F3)</button>
      <button type="button">Clear (F4)</button>
      <button type="button">Refresh (F5)</button>
    </div>
  </div>
</body>
</html>
```

# Notes:
- Ensure proper error handling for fields such as invalid date formats or out-of-range numerical inputs (if applicable).
- Use CSS for styling and layout, keeping the design simple and functional.

BMS Screen:
{CODE}"""


@logger.catch
def modernize_bms(screen_string: str):
    try:
        llm = get_llm(model_type="assistant")
        prompt = INSTRUCTION.format(CODE=screen_string)
        output = llm.invoke(prompt)
        return output
    except Exception as e:
        logger.error(f"Error modernizing BMS screen: {e}")
        return None