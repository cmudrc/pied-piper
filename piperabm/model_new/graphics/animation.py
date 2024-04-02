import os
import shutil
import subprocess


class Animation:
    """
    Manages animation rendering using plt
    """

    def __init__(self, path):
        self.file_names = []
        self.path = path
        self.render_path = os.path.join(self.path, 'render')
        self._clear_folder(self.render_path)
        os.makedirs(self.render_path, exist_ok=True)

    def add_name(self, name):
        """
        Append new filename
        """
        self.file_names.append(name)

    def add_figure(self, fig):
        """
        Add new plt figure to the instance
        """
        file_name = self.new_name()
        file_path = os.path.join(self.render_path, file_name)
        fig.savefig(file_path)
        self.file_names.append(file_path)

    def new_name(self):
        """
        Generate new filename
        """
        length = len(self.file_names)
        name = f"image_{length + 1:04d}.png"
        return name

    def render(self, output_file='output', framerate=10):
        """
        Create animation
        """
        output_file = os.path.join(self.path, output_file + '.mp4')
        
        if not self.file_names:
            print("No images to render.")
            return

        # Command to combine images into a video using ffmpeg
        cmd = [
            'ffmpeg', '-y', '-framerate', str(framerate), '-i',
            os.path.join(self.render_path, 'image_%04d.png'),
            '-c:v', 'libx264', '-pix_fmt', 'yuv420p', output_file
        ]

        subprocess.run(cmd, check=True)
        print(f"Rendered video saved as {output_file}")

        # Clear the render folder after rendering
        self._clear_folder(self.render_path)

    def _clear_folder(self, folder):
        """
        Delete a folder
        """
        if os.path.exists(folder):
            shutil.rmtree(folder)


if __name__ == '__main__':

    import numpy as np
    from matplotlib import pyplot as plt


    class Model:

        def __init__(self, pos, velocity, step_size):
            self.pos = np.array(pos)
            self.velocity = np.array(velocity)
            self.step_size = step_size

        def update(self):
            self.pos += self.velocity * self.step_size

        def fig(self):
            plt.clf()
            ax = plt.gca()
            ax.set_aspect("equal")
            ax.scatter(self.pos[0], self.pos[1])
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            return plt.gcf()
        
        def show(self):
            fig = self.fig()
            plt.show()

    
    model = Model(
        pos=[-10, -10], # meter
        velocity=[1, 1], # meter / second
        step_size=1 # second
    )

    path = os.path.dirname(os.path.realpath(__file__))
    animation = Animation(path)

    for _ in range(21):
        fig = model.fig()
        animation.add_figure(fig)
        model.update()

    animation.render()
