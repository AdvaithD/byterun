class VirtualMachineError(Exception):
    pass


class VirtualMachine(object):
    def __init__(self):
        self.frames = []  # call stack of frames
        self.frame = None  # current frame
        self.return_value = None
        self.last_exception = None

    def run_code(self, code, global_names=None, local_names=None):
        # entry point to execute code
        frame = self.make_frame(
            code, global_names=global_names, local_names=local_names)
        self.run_frame(frame)

    def make_frame(self, code, callargs={}, global_names=None, local_names=None):
        if global_names is not None and local_names is not None:
            local_names = global_names
        elif self.frames:
            global_names = self.frame.global_frames
            local_names = {}
        else:
            global_names = local_names = {
                '__builtins__': __builtins__,
                '__name__': '__main__',
                '__doc__': None,
                '__package__': None,
            }
        local_names.update(callargs)
        frame = Frame(code, global_names, local_names, self.frame)
        return frame
