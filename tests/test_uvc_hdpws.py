#!/usr/bin/env python

"""Tests for `uvc_hdpws` package."""

from uv.models import models


def test_unternehmen():
    novareto = models.Unternehmen(
        name1="Z1",
        name2="Z2",
        strasse="Karolinenstr. 17",
        plz="90763",
        ort="Fürth",
    )
    assert novareto.name1 == "Z1"
    assert novareto.name2 == "Z2"
    assert novareto.strasse == "Karolinenstr. 17"
    assert novareto.plz == "90763"
    assert novareto.ort == "Fürth"
