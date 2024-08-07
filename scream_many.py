import sys

class ScreamingOutput:
    def __init__(self, path=None):
        if path is not None:
            self.file = open(path, "w")
        else:
            self.file = None

    def write(self, string):
        all_caps = string.upper()
        if self.file is not None:
            self.file.write(all_caps)
        else:
            sys.stdout.write(all_caps)

    def close(self):
        if self.file is not None:
            self.file.close()

def open_outputs(paths):
    outputs = []
    try:
        for path in paths:
            outputs.append(ScreamingOutput(path))
        return outputs
    except Exception:
        for output in outputs:
            output.close()
        raise

outputs = open_outputs(sys.argv[1:])
try:
    for output in outputs:
        output.write("hello world\n")
finally:
    for output in outputs:
        output.close()
