import os
import base64
import zlib

from k3d import Plot as _Plot


class Plot(_Plot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def export_animation(self, filename: str):

        with open(os.path.join(os.path.dirname(__file__), 'static', 'snapshot_standalone.txt'), 'r') as file:
            template = file.read()

        with open(os.path.join(os.path.dirname(__file__), 'static', 'standalone.js'), 'r') as file:
            template = template.replace('[K3D_SOURCE]',
                                        base64.b64encode(zlib.compress(file.read().encode())).decode('utf-8'))

        with open(os.path.join(os.path.dirname(__file__), 'static', 'require.js'), 'r') as file:
            template = template.replace('[REQUIRE_JS]', file.read())

        with open(os.path.join(os.path.dirname(__file__), 'static', 'fflate.js'), 'r') as file:
            template = template.replace('[FFLATE_JS]', file.read())

        data = self.get_binary_snapshot()
        template = template.replace('[DATA]', base64.b64encode(data).decode('utf-8'))
        template = template.replace('[ADDITIONAL]', '')

        filename = f'{filename}.html' if len(filename.split('.')) == 1 else filename
        with open(filename, 'w') as file:
            file.write(template)
