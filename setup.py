from setuptools import setup, find_packages

setup(
    name = 'plutonium-plugin-output-transmission',
    description = 'Transmission output plugin for Plutonium',
    version = '1.0',
    install_requires = [
        'plutonium == 1.0',
        'transmissionrpc == 1.0',
    ],
    include_package_data = True,
    packages = find_packages(),
)

