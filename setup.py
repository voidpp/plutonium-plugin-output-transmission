from setuptools import setup, find_packages

setup(
    name = 'plutonium-plugin-output-transmission',
    description = 'Transmission output plugin for Plutonium',
    version = '0.1',
    install_requires = [
        'plutonium',
        'sqlchemyforms',
        'transmissionrpc',
    ],
    include_package_data = True,
    packages = find_packages(),
)

