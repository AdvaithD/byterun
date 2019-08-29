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
