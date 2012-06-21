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

from pylons import tmpl_context
from tw.forms import TextField

from mediacore.lib.i18n import N_
from mediacore.model import Media
from mediacore.plugin import events
from mediacore.plugin.events import observes

@observes(events.Admin.MediaForm)
def append_fields(form):
    f =  TextField('view_count',
            label_text=N_('View Count', domain='mediacore_editviews'),
            attrs={'style': 'width: 68px;'},
            help_text=N_('Set the number of views for this media.',
                         domain='mediacore_editviews'))
    form.children.append(f)

@observes(events.Admin.MediaController.edit)
def populate_fields(**result):
    media = result['media']
    result['media_values'].setdefault('view_count', media.views)
    return result

@observes(events.Admin.MediaController.save)
def save_fields(**result):
    media = Media.query.get(result['media_id'])
    view_count = tmpl_context.form_values.get('view_count', None)
    if view_count is not None:
        media.views = view_count
    return result
