"""reddit's end-of-year charity donation process.


"""

from pylons.i18n import N_

from r2.config.routing import not_in_sr
from r2.lib.js import LocalizedModule
from r2.lib.plugin import Plugin


class Donate(Plugin):
    needs_static_build = True

    errors = {
        "DONATE_UNKNOWN_ORGANIZATION":
            N_("unknown organization"),
        "DONATE_ACCOUNT_NOT_ELIGIBLE":
            N_("account not old enough"),
    }

    js = {
        "donate": LocalizedModule("donate.js",
            # TODO: fill me with code
        ),
    }

    def add_routes(self, mc):
        mc(
            "/donate/organizations/:organization",
            controller="donate",
            action="organization",
            conditions={"function": not_in_sr},
        )

        mc(
            "/donate/organizations",
            controller="donate",
            action="search",
            conditions={"function": not_in_sr},
        )

        mc(
            "/donate/nominations",
            controller="donate",
            action="nominations",
            conditions={"function": not_in_sr},
        )

        mc(
            "/donate",
            controller="donate",
            action="landing",
            conditions={"function": not_in_sr},
        )

        mc(
            "/api/donate/:action",
            controller="donate",
            conditions={"function": not_in_sr},
        )


    def load_controllers(self):
        from reddit_donate.controllers import (
            DonateController,
        )
