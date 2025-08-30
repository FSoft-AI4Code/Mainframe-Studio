import { ElementViews } from "@store";

export const overview = {
  question: "How can I migrate my legacy source code?",
  reply_pre_process: "First of all, let me breakdown the assets and walk you through the process.",
  reply_post_process: `# IBM Mainframe Source Code Repository - Asset Analysis Report

## Asset Breakdown:

- **COPY Files:** 46
- **JCL_IBM Files:** 46
- **COBOL Files:** 28
- **BMS Files:** 18
- **OTHER Files:** 15

## Code Quality Analysis:

- **Actual Code Lines:** 91.58%
- **Commented Lines:** 8.42%

## Key Insights:

- The repository consists mainly of COPY and JCL_IBM files, each contributing 46 assets.
- COBOL source files are fewer (28), but crucial for business logic.
- Comment density is relatively low (8.42%), suggesting room for improved documentation.
- A well-balanced code-to-comment ratio is essential for maintainability and future migrations.`
};

export const assessment = {
  question: "What are the main challenges in migrating this codebase ?",
  reply_pre_process: "Let's identify the main challenges in migrating the codebase.",
  reply_post_process: `## IBM Mainframe Source Code Assessment - Summary Report
### 1. Codebase Overview
#### Total Lines of Code (LoC) by File Type:
- **COBOL:** 15,041 LoC
- **COPY:** 7,686 LoC
- **BMS:** 4,282 LoC
- **JCL_IBM:** 2,872 LoC
- **OTHER:** 1,398 LoC

### 2. Code Complexity Analysis
The complexity distribution shows that most components have low to moderate complexity.
Few components have significantly high complexity (over 200), requiring extra effort during migration.

### 3. Component Decomposition
Majority of components are categorized as low criticality, but some have medium complexity (COTRN02, COUSR00).
High complexity components should be prioritized for modular refactoring.

### 4. Dead Code Assessment
258 out of 1,307 components (≈ 20%) are identified as dead code.
38% complexity reduction is possible by eliminating dead code.
Major dead code areas: 
- **PRTCATBL:** 134 LoC, complexity 128
- **CORPT00:** 421 LoC, complexity 231
- **COCRDLI:** 353 LoC, complexity 43.

## Main Challenges in Migrating the Codebase
- **High Complexity Modules:** Some COBOL and JCL modules have high complexity (above 200), requiring careful refactoring or re-engineering.
- **Significant Dead Code:** A large portion of dead code (20%) adds unnecessary complexity. It must be removed or handled efficiently.
- **Documentation Deficiency:** With only 8.42% comment density, insufficient documentation may hinder smooth migration and reverse engineering.
- **Interdependencies in Copybooks and JCL:** The COPY files (7,686 LoC) and JCL (2,872 LoC) suggest significant dependencies, making modular migration challenging.
- **Code Standardization Issues:** The mix of COBOL, JCL, and other assets may require custom parsers or AI-driven conversion tools.
`
};

export const exploration = {
  question: "What are the recommended strategies for migrating this codebase ?",
  reply_pre_process:
    "Let's explore the components in your codebase by process Reverse Engineering and Code Analysis.",
  reply_post_process: "Done!"
};

export type MessageRespone = {
  question: string;
  reply_pre_process: string;
  reply_post_process?: string;
};

export const messagesResponse: Record<Exclude<ElementViews, "DEFAULT">, MessageRespone> = {
  OVERVIEW: overview,
  ASSESSMENT: assessment,
  EXPLORATION: exploration
};
