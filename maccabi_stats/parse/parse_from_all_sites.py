#!/usr/bin/python
# -*- coding: utf-8 -*-

from maccabi_stats.parse.maccabi_tlv_site.main_parser import get_parsed_maccabi_games_from_maccabi_site
from maccabi_stats.stats.maccabi_games_stats import MaccabiGamesStats


def parse_maccabi_games_from_all_sites():
    """ Iterate all the sites and merge the output to one list of maccabi games.
    :rtype: maccabi_Stats.stats.maccabi_games_stats.MaccabiGamesStats
    """

    # Parse from maccabi-tlv football site:
    maccabi_games_from_maccabi_tlv_site = get_parsed_maccabi_games_from_maccabi_site()
    return MaccabiGamesStats(maccabi_games_from_maccabi_tlv_site)
