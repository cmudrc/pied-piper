import os


class Renderer:

    def __init__(self, dir=''):
        self.files = {}
        self.dir = dir

    def new_index(self):
        return len(self.files)
    
    def new_frame(self, name):
        index = self.new_index()
        self.files[index] = name

    def file_path(self, index):
        return os.path.join(self.dir, self.files[index])
    
    def render(self, name: str = 'animation'):
        
        path = os.path.join(self.dir, name)
    

if __name__ == "__main__":
    renderer = Renderer()
    renderer.new_frame('img_01')
    print(renderer.file_path(0))