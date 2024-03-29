#   Copyright 2011 Josh Kearney
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import setuptools


setuptools.setup(
    name="wootoff",
    version="0.0.7",
    author="Josh Kearney",
    author_email="josh@jk0.org",
    description="Monitor a wootoff.",
    license="Apache License, Version 2.0",
    url="https://github.com/jk0/wootoff",
    install_requires=[
        "beautifulsoup==3.2.0",
        "SocksiPy-branch"
    ],
    scripts=["bin/wootoff"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)
