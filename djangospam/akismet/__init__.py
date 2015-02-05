# -*- coding: utf-8 -*-

from djangospam.akismet import moderator
import warnings

def register(*args, **kwargs):
    warnings.warn("Using 'register' from djangospam.akismet is deprecated. \
Import it from djangospam.akismet.moderator instead.",\
    category=DeprecationWarning, stacklevel=2)
    return register.moderator(*args, **kwargs)

class AlreadyModerated(moderator.AlreadyModerated):
    def __init__(self, *args, **kwargs):
        warnings.warn("Using 'AlreadyModerated' from djangospam.akismet is \
deprecated. Import it from djangospam.akismet.moderator instead."
        , category=DeprecationWarning, stacklevel=2)
        super(AlreadyModerated, self).__init__(*args, **kwargs)

class Akismet(moderator.AlreadyModerated):
    def __init__(self, *args, **kwargs):
        warnings.warn("Using 'Akismet' from djangospam.akismet is \
deprecated. Import it from djangospam.akismet.moderator instead."
        , category=DeprecationWarning, stacklevel=2)
        super(Akismet, self).__init__(*args, **kwargs)

class AkismetError(moderator.AlreadyModerated):
    def __init__(self, *args, **kwargs):
        warnings.warn("Using 'AkismetError' from djangospam.akismet is \
deprecated. Import it from djangospam.akismet.moderator instead."
        , category=DeprecationWarning, stacklevel=2)
        super(AkismetError, self).__init__(*args, **kwargs)
