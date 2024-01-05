import base64
import zlib
import marshal

def obfuscate_and_encode(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    # Split the content into chunks
    chunk_size = 100  # You can adjust this to suit your needs
    chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]

    obfuscated_variables = []

    for i, chunk in enumerate(chunks):
        # Obfuscate content using marshal and zlib
        obfuscated_content = marshal.dumps(chunk.encode())
        obfuscated_content = zlib.compress(obfuscated_content)
        obfuscated_content = base64.b64encode(obfuscated_content).decode()

        # Create variable name dynamically
        variable_name = f'var_{i}'

        # Save the obfuscated content to the variable
        obfuscated_variables.append(obfuscated_content)

    # Combine variables
    compiled_code = 'combined_code = ['
    for obfuscated_content in obfuscated_variables:
        compiled_code += f'"{obfuscated_content}", '
    compiled_code = compiled_code[:-2]  # Remove the trailing comma and space
    compiled_code += ']\n'

    # Decode and execute the combined code
    compiled_code += 'decoded_code = "".join([__import__("base64").b64decode(chunk.encode()).decode(errors="ignore") for chunk in combined_code])\n'
    compiled_code += '__import__("marshal").loads(decoded_code)\n'

    # Save the compiled code to the output file
    with open(output_file, 'w') as output_file:
        output_file.write(compiled_code)

    print(f"File {input_file} has been obfuscated and encoded. Output saved to {output_file}.")

if __name__ == "__main__":
    input_file = "tes.py"
    output_file = "obfuscated_output.py"

    obfuscate_and_encode(input_file, output_file)
