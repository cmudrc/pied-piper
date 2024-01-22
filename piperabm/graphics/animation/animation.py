import os
import shutil
import subprocess
#import matplotlib.pyplot as plt

class Animation:
    def __init__(self):
        self.file_names = []
        self.render_folder = 'render'
        self._clear_folder(self.render_folder)
        os.makedirs(self.render_folder, exist_ok=True)

    def add_name(self, name):
        self.file_names.append(name)

    def add_figure(self, fig):
        file_name = self.new_name()
        file_path = os.path.join(self.render_folder, file_name)
        fig.savefig(file_path)
        self.file_names.append(file_path)

    def new_name(self):
        length = len(self.file_names)
        name = f"image_{length + 1:04d}.png"
        return name

    def render(self, output_file='output', framerate=10):
        output_file += '.mp4'
        if not self.file_names:
            print("No images to render.")
            return

        # Command to combine images into a video using ffmpeg
        cmd = [
            'ffmpeg', '-y', '-framerate', str(framerate), '-i',
            os.path.join(self.render_folder, 'image_%04d.png'),
            '-c:v', 'libx264', '-pix_fmt', 'yuv420p', output_file
        ]

        subprocess.run(cmd, check=True)
        print(f"Rendered video saved as {output_file}")

        # Clear the render folder after rendering
        self._clear_folder(self.render_folder)

    def _clear_folder(self, folder):
        if os.path.exists(folder):
            shutil.rmtree(folder)

