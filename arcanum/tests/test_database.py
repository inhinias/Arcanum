import pytest
from components import dab
class TestDab():
    def test_Connection():
        connec = dab.DatabaseActions.connect("galenite", "pnR(z*j(xp85Sqf(", "kennethmathis.ch", 3306)
        assert connec

    def teardown_connection():
        dab.DatabaseActions.closeEverything()

    def test_Ammount():
        tables = ["passwords", "configs"]
        for i in range(len(tables)):
            assert dab.DatabaseActions.getAmmount(tables[i]) >= 0

