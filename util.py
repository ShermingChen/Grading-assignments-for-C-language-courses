import html
import unicodedata
import os
import subprocess
import codecs
from cffi import FFI


def WriteInTXT(source, filename):
    formatted_source = html.unescape(source).replace('\\r', '')
    formatted_source = unicodedata.normalize('NFKC', formatted_source)
    formatted_source = formatted_source.replace('　', ' ')
    formatted_source = formatted_source.replace(r'\\n', '_special_newline_')
    formatted_source = formatted_source.replace('\\n', '\n')
    formatted_source = formatted_source.replace('\\t', '')
    
    formatted_source = formatted_source.replace('_special_newline_', '\\n')
    formatted_source = '\n'.join(line.strip() for line in formatted_source.splitlines())
    if formatted_source.startswith('[') and formatted_source.endswith(']'):
        formatted_source = formatted_source[2:-2]
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(formatted_source)
    return formatted_source

# # gcc
# def ExecuteCProgram(test_in, expect_out, file_path):    
#     gcc_path = r"C:\MinGW\bin\gcc.exe"
    with codecs.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        c_code = f.read()  
        
    temp_c_file = r"F:\temp.c"
    with open(temp_c_file, 'w', encoding='utf-8') as f:
        f.write(c_code)

    executable_file = os.path.splitext(file_path)[0] + '.exe'
    compile_command = [gcc_path, temp_c_file, "-o", executable_file]

    try:
        process = subprocess.Popen(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        compile_output, compile_error = process.communicate()

        if process.returncode != 0:
            return 3, "compile_error"
        
        if os.path.exists(executable_file):            
            process = subprocess.Popen([executable_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, text=True,encoding = 'utf-8')
            # if label_ == 4:
            #     print(test_in)
            #     test_in = f"{test_in[0]}\n{' '.join(map(str, test_in[1]))}\n"
            #     print(test_in)
            # else:
                # test_in = str(test_in)
            test_in = str(test_in)
            try:
                stdout, stderr = process.communicate(input=test_in, timeout=5)
            except Exception as exc:
                return 3, "Exception, possible infinite loop detected"
            if process.returncode != 0:
                # print(f'{file_path}执行失败，错误信息为: {stderr}')
                return 3, "Execution failed"

    finally:
        if process.returncode == 0:
            # print(stdout)
            if os.path.exists(temp_c_file):
                os.remove(temp_c_file)
                os.remove(executable_file)
            # print(stdout.strip())
            if stdout.strip() == str(expect_out):
                # print('right')
                return 5, ' '
            else:
                print(file_path, "C程序执行结果错误:", stdout.strip())
                return 4, 'The result is wrong!'

# CFFI
def ExecuteCProgram(test_in, expect_out, file_path):    
    ffi = FFI()

    # Read C source code from the file
    with codecs.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        c_code = f.read()

    # Attempt to compile and link the C code
    try:
        # Verify the C code (compilation step)
        compiled_c = ffi.verify(c_code)

        # Prepare the input as C-style strings
        if isinstance(test_in, (list, tuple)):
            test_in = " ".join(map(str, test_in))
        test_in_c = ffi.new("char[]", test_in.encode("utf-8"))

        # Define a buffer for the output
        output_buffer_size = 1024
        output_buffer = ffi.new(f"char[{output_buffer_size}]")

        # Call the C function
        result = compiled_c.main(test_in_c, output_buffer, output_buffer_size)

        # Decode the output buffer
        output = ffi.string(output_buffer).decode("utf-8").strip()

        # Check the result
        if output == str(expect_out):
            return 5, " "
        else:
            return 4, "The result is wrong!"

    except Exception as e:
        return 3, f"Error executing C program: {str(e)}"