"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle


def compile_static_assets(assets):
    """Create stylesheet bundles."""
    assets.auto_build = True
    assets.debug = False
    common_style_bundle = Bundle(
        'src/less/*.less',
        filters='less,cssmin',
        output='dist/css/style.css',
        extra={'rel': 'stylesheet/less'}
    )
    main_style_bundle = Bundle(
        'main_bp/less/main.less',
        filters='less,cssmin',
        output='dist/css/main.css',
        extra={'rel': 'stylesheet/less'}
    )
    profile_style_bundle = Bundle(
        'profile_bp/less/profile.less',
        filters='less,cssmin',
        output='dist/css/profile.css',
        extra={'rel': 'stylesheet/less'}
    )
    assets.register('common_style_bundle', common_style_bundle)
    assets.register('home_style_bundle', main_style_bundle)
    assets.register('profile_style_bundle', profile_style_bundle)
    if app.config['FLASK_ENV'] == 'development':
        common_style_bundle.build()
        main_style_bundle.build()
        profile_style_bundle.build()
    return assets