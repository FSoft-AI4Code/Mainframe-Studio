# This script manages and maps properties to create values.yaml file for the chart

# Color table
reset="\033[0m"
red="\033[0;31m"
magenta="\033[0;35m"
green="\033[1;32m"

# Initiate varibales
properties_file=".env"
values_template_directory="./helm-charts/values-template.yaml"
values_directory_output="./helm-charts/values.yaml"
sed '/^[#\/$].*/d' ${values_template_directory} > ${values_directory_output}

secret_files=${properties_directory}/secrets

# Check yq installed?
yq_installed=`which yq`

if command -v yq >/dev/null 2>&1; then
    echo -e "${green}yq is installed${reset}"
else
    echo -e "${red}yq is not installed${reset}"
    echo -e "${magenta}#macOS using Homebrew \nbrew install yq \n# Linux using wget \nwget https://github.com/mikefarah/yq/releases/download/v4.30.8/yq_linux_amd64 -O /usr/bin/yq && chmod +x /usr/bin/yq${reset}"
    exit
fi

# Setup Secrets

if [ -f "$properties_file" ]; then
    echo -e "${magenta}Opened file ${properties_file} ${reset}"
    while IFS= read -r line; do
        # Ingnore comment lines
        if [[ $line == \#* ]]; then
            continue
        fi
        key=$(echo $line | awk -F'=' '{print $1}')
        value=$(echo $line | awk -F'=' '{print $2}')
        # base64_value=$(echo ${value} | base64 )
        base64_value=$(echo $value | awk '{gsub(/"/, ""); print}')
        yq -i ".configmaps.${key}=\"${base64_value}\"" ${values_directory_output}
        echo -e "${green}Injected ${key}: ${value} to values.yaml${reset}"
    done < ${properties_file}
fi


# Exception cases
# sed -i "s/'''/'/g" ${values_directory_output}
# sed -i "s/]\'/\"]\'/g" ${values_directory_output}
# sed -i "s/\'\[/\'\[\"/g" ${values_directory_output}
# sed -i "s/, /\",\"/" ${values_directory_output}