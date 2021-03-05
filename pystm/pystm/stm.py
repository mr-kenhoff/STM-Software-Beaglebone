
from os.path import join

class STM:

    SYSFS_BASE_PATH = "/sys/devices/virtual/misc/stm"
    DEV_FILEPATH    = "/dev/stm"

    DEFAULT_CONFIG = {
        "dac_calibration": {
            "x_scale": 1,
            "x_offset": 0,
            "y_scale": 1,
            "y_offset": 0,
            "z_scale": 1,
            "z_offset": 0
        },
        "adc_calibration": {
            "scale": 1,
            "offset": 0
        }
    }

    def __init__(self, dev_filepath = DEV_FILEPATH, sysfs_dir = SYSFS_BASE_PATH):
        self.sysfs_files = {
            "ADC_VALUE":           open(join(sysfs_dir, "adc_value"), "r"),
            "PID_SETPOINT":        open(join(sysfs_dir, "pid_setpoint"), "r+"),
            "DAC_X":               open(join(sysfs_dir, "dac_x"), "r+"),
            "DAC_Y":               open(join(sysfs_dir, "dac_y"), "r+"),
            "DAC_Z":               open(join(sysfs_dir, "dac_z"), "r+"),
            "SCAN_ENABLE":         open(join(sysfs_dir, "scan_enable"), "r+"),
            "PID_ENABLE":          open(join(sysfs_dir, "pid_enable"), "r+"),
            "PATTERN_BUFFER_SIZE": open(join(sysfs_dir, "pattern_buffer_size"), "r+"),
            "PATTERN_BUFFER_USED": open(join(sysfs_dir, "pattern_buffer_used"), "r"),
            "BIAS_VOLTAGE":        open(join(sysfs_dir, "bias_voltage"), "r+")
        }

        self.dev_file = open(dev_filepath, "wb")

        self.config = self.DEFAULT_CONFIG

    def get_adc_value(self):
        return int(self.sysfs_files["ADC_VALUE"].read())

    def set_pid_setpoint(self, setpoint):
        self.sysfs_files["PID_SETPOINT"].write(str(setpoint))

    def get_pid_setpoint(self):
        return int(self.sysfs_files["PID_SETPOINT"].read())

    def set_dac_x(self, dac_value):
        self.sysfs_files["DAC_X"].write(str(dac_value))

    def get_dac_x(self):
        return int(self.sysfs_files["DAC_X"].read())

    def set_dac_y(self, dac_value):
        self.sysfs_files["DAC_Y"].write(str(dac_value))

    def get_dac_y(self):
        return int(self.sysfs_files["DAC_Y"].read())

    def set_dac_z(self, dac_value):
        self.sysfs_files["DAC_Z"].write(str(dac_value))

    def get_dac_z(self):
        return int(self.sysfs_files["DAC_Z"].read())

    def set_scan_enable(self, enable):
        assert enable in [0, 1, False, True]
        self.sysfs_files["SCAN_ENABLE"].write(str(int(enable)))

    def get_scan_enable(self):
        return bool(self.sysfs_files["SCAN_ENABLE"].read())

    def set_pid_enable(self, enable):
        assert enable in [0, 1, False, True]
        self.sysfs_files["PID_ENABLE"].write(str(int(enable)))

    def get_pid_enable(self):
        return bool(self.sysfs_files["PID_ENABLE"].read())

    def set_pattern_buffer_size(self, size):
        self.sysfs_files["PATTERN_BUFFER_SIZE"].write(str(size))

    def get_pattern_buffer_size(self):
        return int(self.sysfs_files["PATTERN_BUFFER_SIZE"].read())

    def get_pattern_buffer_used(self):
        return int(self.sysfs_files["PATTERN_BUFFER_USED"].read())

    def set_bias_voltage(self, boltage):
        self.sysfs_files["BIAS_VOLTAGE"].write(str(boltage))

    def get_bias_voltage(self):
        return int(self.sysfs_files["BIAS_VOLTAGE"].read())

    def write_pattern(self, pattern):
        self.dev_file.write(pattern)


if __name__ == '__main__':
    stm = STM()
    stm.set_dac_x(100000)
    print(stm.get_dac_x())