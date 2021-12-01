from setuptools import setup, find_packages

setup(
      name="hzb_shim",
      author = "Ed Rial",
      version = "0.1",
      description='Python transposition of HZB Shim process. Improvement Developments',
      #dependency_links=['http://github.com/ochubar/Radia/tarball/master#egg=package-1.0&subdirectory=env/radia_python',
      #                  'http://github.com/eddrial/wradia/tarball/master#egg=package-1.0'],
      packages = find_packages()#,
#      install_requires = ['some-pkg @ git+https://github.com/eddrial/wRadia@master']#,
#                          'radia',
#                          ''],
#     # package_data={'': ['radia_py3_7_x86_64.so']},
      )
#
