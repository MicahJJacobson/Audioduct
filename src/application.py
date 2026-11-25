import subprocess

def make_channel(name: str, real_sink: str):
    subprocess.run("pactl", "load-module", "module-null-sink", f"sink-name={name}", f"sink-properties=device.description={name}")


