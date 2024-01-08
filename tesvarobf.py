import base64
import zlib
import marshal

def obfuscate_and_encode(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content into chunks
    chunk_size = 100  # You can adjust this to suit your needs
    chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]

    obfuscated_variables = []

    for i, chunk in enumerate(chunks):
        # Obfuscate content using marshal and zlib
        obfuscated_content = marshal.dumps(chunk.encode())
        obfuscated_content = zlib.compress(obfuscated_content)
        obfuscated_content = base64.b64encode(obfuscated_content).decode(errors="ignore")

        # Create variable name dynamically
        variable_name = f'var_{i}'

        # Save the obfuscated content to the variable
        obfuscated_variables.append(f'{variable_name} = {obfuscated_content}')

    # Combine variables into a single list
    compiled_code = 'obfuscated_content_list = ['
    for obfuscated_content in obfuscated_variables:
        compiled_code += obfuscated_content + ', '
    compiled_code = compiled_code[:-2]  # Remove the trailing comma and space
    compiled_code += ']\n'

    # Combine the list into bytes
    compiled_code += 'combined_code = b"".join(obfuscated_content_list)\n'

    # Decode and execute the combined code
    compiled_code += '__import__("marshal").loads(combined_code)\n'

    # Save the compiled code to the output file
    with open(output_file, 'wb') as output_file:
        output_file.write(compiled_code.encode('utf-8'))

    print(f"File {input_file} has been obfuscated and encoded. Output saved to {output_file}.")

if __name__ == "__main__":
    input_file = "obf.py"
    output_file = "obfuscated_output.py"

    obfuscate_and_encode(input_file, output_file)
