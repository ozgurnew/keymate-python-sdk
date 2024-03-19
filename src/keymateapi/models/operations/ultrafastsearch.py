"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from keymateapi import utils
from typing import List, Optional


@dataclasses.dataclass
class UltrafastsearchSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclasses.dataclass
class UltrafastsearchRequest:
    q: str = dataclasses.field(metadata={'query_param': { 'field_name': 'q', 'style': 'form', 'explode': True }})
    r"""URL of the website."""
    percentile: str = dataclasses.field(metadata={'query_param': { 'field_name': 'percentile', 'style': 'form', 'explode': True }})
    r"""Set it as '100'"""
    numofpages: str = dataclasses.field(metadata={'query_param': { 'field_name': 'numofpages', 'style': 'form', 'explode': True }})
    r"""Set it as '10'"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UltrafastsearchResponseResponseBody:
    r"""Error fetching search results"""
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    r"""Error message"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UltrafastsearchResults:
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""The title of the search result"""
    link: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link'), 'exclude': lambda f: f is None }})
    r"""The URL of the search result"""
    summary: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summary'), 'exclude': lambda f: f is None }})
    r"""A summary of the HTML content of the search result (available for the first five results)"""
    full_content: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('full_content'), 'exclude': lambda f: f is None }})
    r"""The entire HTML content of the search result (available for the first three results)"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UltrafastsearchResponseBody:
    r"""Successful operation"""
    results: Optional[List[UltrafastsearchResults]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    rules: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rules'), 'exclude': lambda f: f is None }})
    r"""The rules which recommend gpt to follow."""
    



@dataclasses.dataclass
class UltrafastsearchResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    two_hundred_application_json_object: Optional[UltrafastsearchResponseBody] = dataclasses.field(default=None)
    r"""Successful operation"""
    default_application_json_object: Optional[UltrafastsearchResponseResponseBody] = dataclasses.field(default=None)
    r"""Error fetching search results"""
    

