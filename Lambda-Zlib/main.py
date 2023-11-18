import zlib
import os
import sys

# Clear Terminal
def clear_terminal():
    if "linux" in sys.platform.lower():
        os.system('clear')
    elif "win" in sys.platform.lower():
        os.system('cls')

def main():
    try:
        encryption_code = 'exec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(\'\',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),"<Ryougaa-Hideki","exec"))(%s,compile))'

        computer = 0
        input_file = input('Input File : ')
        iteration_count = int(input('Iteration Count : '))

        if iteration_count < 300:
            output_file = input('Output File : ')
            read_original = open(input_file).read()
            compressed_repr = repr(zlib.compress(read_original.encode('utf-8')))
            
            with open(output_file, 'w') as output_file_writer:
                output_file_writer.write(encryption_code % compressed_repr)

            while iteration_count >= computer:
                read_encrypted = open(output_file).read()
                compressed_repr = repr(zlib.compress(read_encrypted.encode('utf-8')))
                
                with open(output_file, 'w') as output_file_writer:
                    output_file_writer.write(encryption_code % compressed_repr)

                print(f'Obfuscating file at iteration {computer}')
                computer += 1

            print(f'Encryption success | File saved as {output_file}')
    except ValueError:
        print('Please enter a valid number for the iteration count')
    except KeyboardInterrupt:
        print('\nEncryption stopped')

if __name__ == '__main__':
    clear_terminal()  # Clear the terminal before starting
    main()
