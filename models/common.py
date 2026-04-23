"""Shared API models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class APIResult:
    raw: dict
