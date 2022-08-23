"""
    Auswärtiges Amt: Reisewarnungen OpenData Schnittstelle

    Reisewarnungen OpenData Schnittstelle. Dies ist die Beschreibung für die Schnittstelle zum Zugriff auf die Daten des [Auswärtigen Amtes](https://www.auswaertiges-amt.de/de/) im Rahmen der [OpenData](https://www.auswaertiges-amt.de/de/open-data-schnittstelle/736118) Initiative. ## Deaktivierung Die Schnittstelle kann deaktiviert werden, in dem Fall wird ein leeres JSON-Objekt zurückgegeben. ## Fehlerfall Im Fehlerfall wird ein leeres JSON-Objekt zurückgegeben. ## Nutzungsbedingungen Die Nutzungsbedingungen sind auf der [OpenData-Schnittstelle](https://www.auswaertiges-amt.de/de/open-data-schnittstelle/736118)  des Auswärtigen Amtes zu finden.   ## Änderungen [(offizielles Changelog)](https://www.auswaertiges-amt.de/de/-/2412916) ### version [1.2.7](https://www.auswaertiges-amt.de/de/-/2412916) - (02.08.2022) Dreistellige ISO-Ländercodes ([ISO 3166-1 alpha-3](https://de.wikipedia.org/wiki/ISO-3166-1-Kodierliste)) wurden als `iso3CountryCode` hinzugefügt. ### version [1.2.6](https://www.auswaertiges-amt.de/de/-/2412916) - (08.12.2021) Es werden zusätzlich zu jedem Land **Ländercodes** mit jeweils **zwei Buchstaben** mit ausgegeben. Die Länderkürzel werden bei [`/travelwarning`](#operations-default-getTravelwarning) und [`/travelwarning/{contentId}`](#operations-default-getSingleTravelwarning) in einem neuen Attribut ausgegeben z.B. in: [`/travelwarning/199124`](https://www.auswaertiges-amt.de/opendata/travelwarning/199124). ### version [1.2.5](https://www.auswaertiges-amt.de/de/-/2412916) (ursprünglich geplant für Ende September 2021) `content` (-> Details des Reise- und Sicherheitshinweis) wurde von [`/travelwarning`](#operations-default-getTravelwarning) entfernt -> bitte ab jetzt [`/travelwarning/{contentId}`](#operations-default-getSingleTravelwarning) nutzen um `content` abzufragen `flagURL` (-> Details des Reise- und Sicherheitshinweis) wurde entfernt -> es werden keine **Flaggen** mehr angeboten  # noqa: E501

    The version of the OpenAPI document: 1.2.6
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.travelwarning.model.reisewarnung import Reisewarnung

from deutschland import travelwarning


class TestReisewarnung(unittest.TestCase):
    """Reisewarnung unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReisewarnung(self):
        """Test Reisewarnung"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Reisewarnung()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
