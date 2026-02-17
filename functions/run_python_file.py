import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.abspath(os.path.join(working_directory_abs, file_path))
        valid_target_dir = os.path.commonpath([working_directory_abs, file_path_abs]) == working_directory_abs
        if not valid_target_dir:
            raise Exception(f'Cannot execute "{file_path}" as it is outside the permitted working directory')

        if not os.path.isfile(file_path_abs):
            raise Exception(f'"{file_path}" does not exists')

        if not ".py" in os.path.basename(file_path_abs):
            raise Exception(f'Error: "{file_path}" is not a Python file')

        command = ["python", file_path_abs]

        if args is not None:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=working_directory_abs,
            capture_output=True,
            text=True,
            timeout=30
        )

        output_string = ""

        if result.returncode != 0:
            output_string += f"Process exited with code {result.returncode}"
        if result.stdout is None or result.stderr is None:
            output_string += "No output produced"
        if result.stdout:
            output_string += f"STDOUT: {result.stdout}"
        if result.stderr:
            output_string += f"STDERR: {result.stderr}"

        return output_string

    except Exception as e:
        raise Exception(f"Error: executing Python file: {e}")