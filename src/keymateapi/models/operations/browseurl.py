"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import browsewithproxyresultitem as components_browsewithproxyresultitem
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from keymateapi import utils
from typing import List, Optional


@dataclasses.dataclass
class BrowseurlRequest:
    inputwindowwords: str = dataclasses.field(metadata={'query_param': { 'field_name': 'inputwindowwords', 'style': 'form', 'explode': True }})
    r"""Always set this !! . Set it as '10000' first if responsetoolarge occurs reduce it to 2000."""
    q: str = dataclasses.field(metadata={'query_param': { 'field_name': 'q', 'style': 'form', 'explode': True }})
    r"""URL of the website."""
    percentile: str = dataclasses.field(metadata={'query_param': { 'field_name': 'percentile', 'style': 'form', 'explode': True }})
    r"""Start it as '1', increase to '2' if ResponseTooLarge occurs you can multiply it with 2 for each retry."""
    numofpages: str = dataclasses.field(metadata={'query_param': { 'field_name': 'numofpages', 'style': 'form', 'explode': True }})
    r"""Set it as '1'"""
    paging: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'paging', 'style': 'form', 'explode': True }})
    r"""Set it as '1' first then according to results you can increase it by one to get the other part of the same page."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BrowseurlResponseResponseBody:
    r"""Error fetching search results"""
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    r"""Error message"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BrowseurlResponseBody:
    r"""Successful operation"""
    currentkeymateuser: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currentkeymateuser'), 'exclude': lambda f: f is None }})
    notice_for_human: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('noticeForHuman'), 'exclude': lambda f: f is None }})
    results: Optional[List[components_browsewithproxyresultitem.BrowsewithProxyResultItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    rules: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rules'), 'exclude': lambda f: f is None }})
    r"""The rules which recommend gpt to follow."""
    



@dataclasses.dataclass
class BrowseurlResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    two_hundred_application_json_object: Optional[BrowseurlResponseBody] = dataclasses.field(default=None)
    r"""Successful operation"""
    default_application_json_object: Optional[BrowseurlResponseResponseBody] = dataclasses.field(default=None)
    r"""Error fetching search results"""
    

