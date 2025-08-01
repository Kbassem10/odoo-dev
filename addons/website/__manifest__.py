# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website',
    'category': 'Website/Website',
    'sequence': 20,
    'summary': 'Enterprise website builder',
    'website': 'https://www.odoo.com/app/website',
    'version': '1.0',
    'depends': [
        'digest',
        'web',
        'web_editor',
        'http_routing',
        'portal',
        'social_media',
        'auth_signup',
        'mail',
        'google_recaptcha',
        'utm',
    ],
    'external_dependencies': {
        'python': ['geoip2'],
    },
    'installable': True,
    'data': [
        # security.xml first, data.xml need the group to exist (checking it)
        'security/website_security.xml',
        'security/ir.model.access.csv',
        'data/image_library.xml',
        'data/ir_asset.xml',
        'data/ir_cron_data.xml',
        'data/mail_mail_data.xml',
        'data/website_data.xml',
        'data/website_visitor_cron.xml',
        'data/digest_data.xml',
        'views/website_templates.xml',
        'views/snippets/snippets.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_text_cover.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_instagram_page.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_alert.xml',
        'views/snippets/s_card.xml',
        'views/snippets/s_share.xml',
        'views/snippets/s_social_media.xml',
        'views/snippets/s_rating.xml',
        'views/snippets/s_hr.xml',
        'views/snippets/s_facebook_page.xml',
        'views/snippets/s_image_gallery.xml',
        'views/snippets/s_countdown.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_comparisons.xml',
        'views/snippets/s_company_team.xml',
        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_references.xml',
        'views/snippets/s_popup.xml',
        'views/snippets/s_faq_collapse.xml',
        'views/snippets/s_features_grid.xml',
        'views/snippets/s_tabs.xml',
        'views/snippets/s_table_of_content.xml',
        'views/snippets/s_chart.xml',
        'views/snippets/s_parallax.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_masonry_block.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_showcase.xml',
        'views/snippets/s_timeline.xml',
        'views/snippets/s_process_steps.xml',
        'views/snippets/s_text_highlight.xml',
        'views/snippets/s_progress_bar.xml',
        'views/snippets/s_blockquote.xml',
        'views/snippets/s_badge.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_mega_menu_multi_menus.xml',
        'views/snippets/s_mega_menu_menu_image_menu.xml',
        'views/snippets/s_mega_menu_thumbnails.xml',
        'views/snippets/s_mega_menu_little_icons.xml',
        'views/snippets/s_mega_menu_images_subtitles.xml',
        'views/snippets/s_mega_menu_menus_logos.xml',
        'views/snippets/s_mega_menu_odoo_menu.xml',
        'views/snippets/s_mega_menu_big_icons_subtitles.xml',
        'views/snippets/s_mega_menu_cards.xml',
        'views/snippets/s_google_map.xml',
        'views/snippets/s_map.xml',
        'views/snippets/s_dynamic_snippet.xml',
        'views/snippets/s_dynamic_snippet_carousel.xml',
        'views/snippets/s_embed_code.xml',
        'views/snippets/s_website_controller_page_listing_layout.xml',
        'views/snippets/s_website_form.xml',
        'views/snippets/s_searchbar.xml',
        'views/snippets/s_button.xml',
        'views/snippets/s_image.xml',
        'views/snippets/s_video.xml',
        'views/new_page_template_templates.xml',
        'views/website_views.xml',
        'views/website_pages_views.xml',
        'views/website_controller_pages_views.xml',
        'views/website_visitor_views.xml',
        'views/res_config_settings_views.xml',
        'views/website_rewrite.xml',
        'views/ir_actions_server_views.xml',
        'views/ir_asset_views.xml',
        'views/ir_attachment_views.xml',
        'views/ir_model_views.xml',
        'views/res_partner_views.xml',
        'views/neutralize_views.xml',
        'wizard/base_language_install_views.xml',
        'wizard/website_robots.xml',
        # Replaces a post_init_hook that should be run on upgrade too.
        'data/update_theme_images.xml',
    ],
    'demo': [
        'data/website_demo.xml',
        'data/website_visitor_demo.xml',
    ],
    'application': True,
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'assets': {
        'web.assets_frontend': [
            ('replace', 'web/static/src/legacy/js/public/public_root_instance.js', 'website/static/src/js/content/website_root_instance.js'),
            'website/static/src/core/errors/beforeunload_error_handler.js',
            'website/static/src/libs/zoomodoo/zoomodoo.scss',
            'website/static/src/scss/website.scss',
            'website/static/src/scss/website_controller_page.scss',
            'website/static/src/scss/website.ui.scss',
            'website/static/src/libs/zoomodoo/zoomodoo.js',
            'website/static/src/libs/bootstrap/bootstrap.js',
            'website/static/src/js/utils.js',
            'web/static/src/core/autocomplete/*',
            'website/static/src/components/autocomplete_with_pages/*',
            'website/static/src/js/tours/tour_utils.js',
            'website/static/src/js/content/website_root.js',
            'website/static/src/js/widgets/dialog.js',
            'website/static/src/js/content/compatibility.js',
            'website/static/src/js/content/menu.js',
            'website/static/src/js/content/snippets.animation.js',
            'website/static/src/js/show_password.js',
            'website/static/src/js/post_link.js',
            'website/static/src/js/plausible.js',
            'website/static/src/js/website_controller_page_listing_layout.js',
            'website/static/src/js/user_custom_javascript.js',
            'website/static/src/js/http_cookie.js',
            'website/static/src/xml/website.xml',
            'website/static/src/xml/website.background.video.xml',
            'website/static/src/xml/website.share.xml',
            'website/static/src/js/text_processing.js',
            # Stable fix, will be replaced by an `ir.asset` in master to be able
            # to clean `<script>` tags in embed code snippets in edit mode.
            'website/static/src/snippets/s_embed_code/000.js',
        ],
        'web.assets_frontend_minimal': [
            'website/static/src/js/content/inject_dom.js',
            'website/static/src/js/content/auto_hide_menu.js',
            'website/static/src/js/content/redirect.js',
            'website/static/src/js/content/adapt_content.js',
        ],
        'web.assets_frontend_lazy': [
            # Remove assets_frontend_minimal
            ('remove', 'website/static/src/js/content/inject_dom.js'),
            ('remove', 'website/static/src/js/content/auto_hide_menu.js'),
            ('remove', 'website/static/src/js/content/redirect.js'),
            ('remove', 'website/static/src/js/content/adapt_content.js'),
        ],
        'web._assets_primary_variables': [
            'website/static/src/scss/primary_variables.scss',
            'website/static/src/scss/options/user_values.scss',
            'website/static/src/scss/options/colors/user_color_palette.scss',
            'website/static/src/scss/options/colors/user_gray_color_palette.scss',
            'website/static/src/scss/options/colors/user_theme_color_palette.scss',
        ],
        'web._assets_secondary_variables': [
            ('prepend', 'website/static/src/scss/secondary_variables.scss'),
        ],
        'web.assets_tests': [
            'website/static/tests/tour_utils/focus_blur_snippets_options.js',
            'website/static/tests/tour_utils/website_preview_test.js',
            'website/static/tests/tour_utils/widget_lifecycle_dep_widget.js',
            'website/static/tests/tours/**/*',
        ],
        'web.assets_backend': [
            ('include', 'website.assets_editor'),
            'website/static/src/scss/color_palettes.scss',
            'website/static/src/scss/view_hierarchy.scss',
            'website/static/src/scss/website.backend.scss',
            'website/static/src/scss/website_visitor_views.scss',
            'website/static/src/js/backend/**/*',
            'website/static/src/js/tours/tour_utils.js',
            'website/static/src/js/text_processing.js',
            'website/static/src/client_actions/*/*',
            'website/static/src/components/fields/*',
            'website/static/src/components/fullscreen_indication/fullscreen_indication.js',
            'website/static/src/components/fullscreen_indication/fullscreen_indication.scss',
            'website/static/src/components/fullscreen_indication/fullscreen_indication.xml',
            'website/static/src/components/website_loader/website_loader.js',
            'website/static/src/components/website_loader/website_loader.scss',
            'website/static/src/components/views/*',
            'website/static/src/services/website_service.js',
            'website/static/src/js/utils.js',
            'web/static/src/core/autocomplete/*',
            'website/static/src/components/autocomplete_with_pages/*',
            'website/static/src/xml/website.xml',

            # Don't include dark mode files in light mode
            ('remove', 'website/static/src/client_actions/*/*.dark.scss'),
        ],
        "web.assets_web_dark": [
            'website/static/src/components/dialog/*.dark.scss',
            'website/static/src/scss/website.backend.dark.scss',
            'website/static/src/client_actions/*/*.dark.scss',
            'website/static/src/components/website_loader/website_loader.dark.scss'
        ],
        'web.qunit_suite_tests': [
            'website/static/tests/redirect_field_tests.js',
        ],
        'web.tests_assets': [
            'website/static/tests/website_service_mock.js',
        ],
        'web._assets_frontend_helpers': [
            ('prepend', 'website/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web_editor.assets_wysiwyg': [
            'website/static/src/js/editor/editor.js',
            '/website/static/src/components/wysiwyg_adapter/toolbar_patch.js',
            'website/static/src/xml/web_editor.xml',
            'website/static/src/js/editor/widget_link.js',
        ],
        'website.assets_wysiwyg': [
            ('include', 'web._assets_helpers'),
            'web_editor/static/src/scss/bootstrap_overridden.scss',
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            'website/static/src/scss/website.wysiwyg.fonts.scss',
            'website/static/src/scss/website.wysiwyg.scss',
            'website/static/src/scss/website.edit_mode.scss',
            'website/static/src/js/editor/snippets.editor.js',
            'website/static/src/js/editor/snippets.options.js',
            'website/static/src/snippets/s_facebook_page/options.js',
            'website/static/src/snippets/s_image_gallery/options.js',
            'website/static/src/snippets/s_image_gallery/000.xml',
            'website/static/src/snippets/s_instagram_page/options.js',
            'website/static/src/snippets/s_countdown/options.js',
            'website/static/src/snippets/s_countdown/options.xml',
            'website/static/src/snippets/s_masonry_block/options.js',
            'website/static/src/snippets/s_popup/options.js',
            'website/static/src/snippets/s_product_catalog/options.js',
            'website/static/src/snippets/s_chart/options.js',
            'website/static/src/snippets/s_rating/options.js',
            'website/static/src/snippets/s_tabs/options.js',
            'website/static/src/snippets/s_progress_bar/options.js',
            'website/static/src/snippets/s_blockquote/options.js',
            'website/static/src/snippets/s_showcase/options.js',
            'website/static/src/snippets/s_table_of_content/options.js',
            'website/static/src/snippets/s_timeline/options.js',
            'website/static/src/snippets/s_media_list/options.js',
            'website/static/src/snippets/s_google_map/options.js',
            'website/static/src/snippets/s_map/options.js',
            'website/static/src/snippets/s_dynamic_snippet/options.js',
            'website/static/src/snippets/s_dynamic_snippet_carousel/options.js',
            'website/static/src/snippets/s_website_controller_page_listing_layout/options.js',
            'website/static/src/snippets/s_website_form/options.js',
            'website/static/src/js/form_editor_registry.js',
            'website/static/src/js/send_mail_form.js',
            'website/static/src/xml/website_form.xml',
            'website/static/src/xml/website.editor.xml',
            'website/static/src/xml/website_form_editor.xml',
            'website/static/src/snippets/s_searchbar/options.js',
            'website/static/src/snippets/s_social_media/options.js',
            'website/static/src/snippets/s_process_steps/options.js',
            'website/static/src/js/editor/widget_link.js',
            'website/static/src/js/widgets/link_popover_widget.js',
            'website/static/src/xml/website.cookies_bar.xml',
            'website/static/src/js/editor/commands_overridden.js',
            'website/static/src/js/editor/odoo_editor.js',
        ],
        'website.assets_all_wysiwyg': [
            ('include', 'web_editor.assets_wysiwyg'),
            ('include', 'web_editor.assets_legacy_wysiwyg'),
            ('include', 'website.assets_wysiwyg'),
        ],
        'website.backend_assets_all_wysiwyg': [
            ('include', 'web_editor.backend_assets_wysiwyg'),
            ('include', 'web_editor.assets_legacy_wysiwyg'),
            ('include', 'website.assets_wysiwyg'),
            'website/static/src/components/wysiwyg_adapter/wysiwyg_adapter.js',
            'website/static/src/snippets/s_embed_code/options.js',
        ],
        # TODO: in master, we should revisit this and probably opt-in what is
        # to be added in the iframe instead of excluding what should not be.
        'website.assets_wysiwyg_inside': [
            ('include', 'website.assets_wysiwyg'),
            ('remove', 'website/static/src/scss/website.wysiwyg.fonts.scss'),
        ],
        'website.assets_all_wysiwyg_inside': [
            ('include', 'website.assets_all_wysiwyg'),
            ('remove', 'website/static/src/scss/website.wysiwyg.fonts.scss'),
        ],
        'web_editor.assets_media_dialog': [
            'website/static/src/components/media_dialog/image_selector.js',
        ],
        'website.assets_editor': [
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            'website/static/src/components/resource_editor/**/*',
            'website/static/src/components/edit_head_body_dialog/edit_head_body_dialog.js',
            'website/static/src/components/edit_head_body_dialog/edit_head_body_dialog.scss',
            'website/static/src/components/edit_head_body_dialog/edit_head_body_dialog.xml',
            'website/static/src/components/dialog/*.js',
            'website/static/src/components/dialog/*.scss',
            'website/static/src/components/dialog/*.xml',
            'website/static/src/components/editor/editor.js',
            'website/static/src/components/editor/editor.scss',
            'website/static/src/components/editor/editor.xml',
            'website/static/src/components/navbar/navbar.js',
            'website/static/src/components/navbar/navbar.scss',
            'website/static/src/components/navbar/navbar.xml',
            'website/static/src/components/burger_menu/burger_menu.js',
            'website/static/src/components/switch/switch.js',
            'website/static/src/components/switch/switch.scss',
            'website/static/src/components/wysiwyg_adapter/page_options.js',
            'website/static/src/components/translator/translator.js',
            'website/static/src/components/translator/translator.scss',
            'website/static/src/components/translator/translator.xml',
            'website/static/src/js/new_content_form.js',
            'website/static/src/services/website_custom_menus.js',
            'website/static/src/js/tours/homepage.js',
            'website/static/src/systray_items/*',
            'website/static/src/client_actions/*/*.xml',
            'website/static/src/components/website_loader/*.xml',
            'website/static/src/js/backend/**/*',

            # Don't include dark mode files in light mode
            ('remove', 'website/static/src/components/dialog/*.dark.scss'),
        ],
    },
    'new_page_templates': {
        'basic': {
            '1': ['s_text_block_h1', 's_text_block', 's_image_text', 's_text_image'],
            '2': ['s_text_block_h1', 's_picture', 's_text_block'],
            '3': ['s_parallax', 's_text_block_h1', 's_text_block', 's_three_columns'],
            '4': ['s_text_cover'],
            '5': ['s_text_block_h1', 's_text_block', 's_features', 's_quotes_carousel'],
            '6': ['s_text_block_h1', 's_table_of_content'],
        },
        'about': {
            'full': ['s_text_block_h1', 's_image_text', 's_text_image', 's_numbers', 's_picture', 's_quotes_carousel', 's_references'],
            'full_1': ['s_text_block_h1', 's_three_columns', 's_text_block_h2', 's_company_team', 's_references', 's_quotes_carousel', 's_call_to_action'],
            'mini': ['s_cover', 's_text_block_h2', 's_text_block_2nd', 's_picture_only', 's_text_block_h2_contact', 's_website_form'],
            'personal': ['s_text_cover', 's_image_text', 's_text_block_h2', 's_numbers', 's_features', 's_call_to_action_about'],
            'map': ['s_text_block_h1', 's_text_block', 's_numbers', 's_text_image', 's_text_block_h2', 's_text_block_2nd', 's_map', 's_images_wall'],
            'timeline': ['s_banner', 's_text_block_h2', 's_text_block', 's_timeline', 's_call_to_action_about'],
        },
        'landing': {
            '0': ['s_cover'],
            '1': ['s_banner', 's_features', 's_masonry_block', 's_call_to_action_digital', 's_references', 's_quotes_carousel'],
            '2': ['s_cover', 's_text_image', 's_text_block_h2', 's_three_columns', 's_call_to_action'],
            '3': ['s_text_cover', 's_text_block_h2', 's_three_columns', 's_showcase', 's_color_blocks_2', 's_quotes_carousel', 's_call_to_action'],
            '4': ['s_cover', 's_text_block_h2', 's_text_block', 's_text_block_h2_contact', 's_website_form'],
            '5': ['s_banner'],
        },
        'gallery': {
            '0': ['s_text_block_h2', 's_images_wall'],
            '1': ['s_text_block_h2', 's_image_text', 's_text_image', 's_image_text_2nd'],
            '2': ['s_banner', 's_text_block_2nd', 's_image_gallery', 's_picture_only'],
            '3': ['s_text_block_h2', 's_text_block', 's_three_columns', 's_three_columns_2nd'],
            '4': ['s_cover', 's_media_list'],
        },
        'services': {
            '0': ['s_text_block_h1', 's_text_block_2nd', 's_three_columns', 's_text_block_h2_contact', 's_website_form'],
            '1': ['s_text_block_h1', 's_features_grid', 's_text_block_h2', 's_faq_collapse', 's_call_to_action'],
            '2': ['s_text_cover', 's_image_text', 's_text_image', 's_image_text_2nd', 's_call_to_action_digital'],
            '3': ['s_text_block_h1', 's_parallax', 's_table_of_content', 's_call_to_action'],
        },
        'pricing': {
            '0': ['s_text_block_h1', 's_comparisons', 's_text_block_2nd', 's_showcase', 's_text_block_h2', 's_faq_collapse', 's_call_to_action'],
            '1': ['s_text_block_h1', 's_comparisons', 's_call_to_action'],
            '2': ['s_cover', 's_comparisons', 's_call_to_action', 's_features_grid', 's_color_blocks_2'],
            '3': ['s_carousel', 's_product_catalog', 's_call_to_action_menu'],  # should be s_call_to_action - but let's create that snippet
            '4': ['s_text_block_h1', 's_image_text', 's_text_image', 's_image_text_2nd', 's_call_to_action'],
            '5': ['s_text_block_h1', 's_text_block', 's_product_catalog', 's_three_columns_menu', 's_call_to_action'],  # was s_call_to_action_menu
        },
        'team': {
            '0': ['s_text_block_h1', 's_three_columns'],
            '1': ['s_text_block_h1', 's_image_text', 's_text_image', 's_image_text_2nd'],
            '2': ['s_text_block_h1', 's_company_team'],
            '3': ['s_text_block_h1', 's_media_list'],
            '4': ['s_text_block_h1', 's_text_block', 's_images_wall'],
            '5': ['s_text_block_h1', 's_text_block', 's_image_gallery', 's_picture'],
        },
    },
    'license': 'LGPL-3',
}
