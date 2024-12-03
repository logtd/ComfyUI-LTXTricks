class AttentionBank:
    def __init__(self, save_steps, block_map, inject_steps=None):
        self._data = {
            'save_steps': save_steps,
            'block_map': block_map,
            'inject_steps': inject_steps,
        }
    
    def __getitem__(self, key):
        return self._data[key]
    
    def __setitem__(self, key, value):
        self._data[key] = value

    def get(self, key, default=None):
        return self._data.get(key, default)

