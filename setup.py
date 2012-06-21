# This file is a part of MediaCoreEditViews, Copyright 2010 Simple Station Inc.
#
# MediaCore is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MediaCore is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name = 'MediaCore-EditViews',
    version = '0.9.0b1',
    packages = find_packages(),
    author = 'Simple Station Inc.',
    author_email = 'info@simplestation.com',
    description = 'A MediaCore plugin to allow an administrator to edit the view count of a media item.',
    install_requires = [
        'MediaCore >= 0.9.0b1',
    ],
    entry_points = {
        'mediacore.plugin': ['editviews = mediacore_editviews'],
    },
    message_extractors = {'mediacore_editviews': [
        ('**.py', 'python', None),
        ('templates/**.html', 'genshi', {'template_class': 'genshi.template.markup:MarkupTemplate'}),
        ('public/**', 'ignore', None),
        ('tests/**', 'ignore', None),
    ]},
)
