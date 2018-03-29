# -*- coding: utf-8 -*-


from maccabistats.config.config import get_int_from_settings, get_str_from_settings, get_bool_from_settings

# This file contains all the settings.ini file related

section_name_in_settings = "maccabi-site"

max_seasons = "max-seasons-to-crawl"
season_page_pattern = "season-page-pattern"
folder_to_save_seasons_html_files = "folder-to-save-seasons-html-files"
folder_to_save_games_html_files = "folder-to-save-games-html-files"
should_use_disk_to_crawl_when_available = "use-disk-to-crawl-when-available"
use_lxml_parser = "use-lxml-parser"


def get_use_lxml_parser_from_settings():
    return get_bool_from_settings(section_name_in_settings, use_lxml_parser)


def get_should_use_disk_to_crawl_when_available_from_settings():
    return get_bool_from_settings(section_name_in_settings, should_use_disk_to_crawl_when_available)


def get_max_seasons_from_settings():
    return get_int_from_settings(section_name_in_settings, max_seasons)


def get_season_page_pattern_from_settings():
    return get_str_from_settings(section_name_in_settings, season_page_pattern)


def get_folder_to_save_seasons_html_files_from_settings():
    return get_str_from_settings(section_name_in_settings, folder_to_save_seasons_html_files)


def get_folder_to_save_games_html_files_from_settings():
    return get_str_from_settings(section_name_in_settings, folder_to_save_games_html_files)
