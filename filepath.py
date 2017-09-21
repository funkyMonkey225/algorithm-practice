class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        new_path = new_path.split('/')
        old_path = self.current_path.split('/')
        for i in range(len(new_path)):
            if new_path[i] == "..":
                old_path.pop(len(old_path) - 1)
                print(old_path)
            else:
                old_path.append(new_path[i])
        print(old_path)
        self.current_path = '/'.join(old_path)
                

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)

path = Path('/a/b/c/d')
path.cd('../x/y/../z')
print(path.current_path)