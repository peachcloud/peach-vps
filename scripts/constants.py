# constants
MICROSERVICES_SRC_DIR = "/srv/peachcloud/automation/microservices"
WEB_DIR = "/var/www/"
APT_DIR = "/var/www/apt.peachcloud.org"
DEBIAN_REPO_DIR = "/var/www/apt.peachcloud.org/debian"
DEBIAN_REPO_CONF_DIR = "/var/www/apt.peachcloud.org/debian/conf"

# before running this script run `gpg --gen-key` on the server, and put the key id here
# `gpg --list-keys`
GPG_KEY_ID = "4ACEF251EA3E091167E8F03EBF69A52BE3565476"

SERVICES = [
    {"name": "peach-oled", "repo_url": "https://github.com/peachcloud/peach-oled.git"},
    {"name": "peach-network", "repo_url": "https://github.com/peachcloud/peach-network.git"},
    {"name": "peach-stats", "repo_url": "https://github.com/peachcloud/peach-stats.git"},
    # {"name": "peach-web", "repo_url": "https://github.com/peachcloud/peach-web.git"}, # currently build fails because it needs rust nightly for pear
    {"name": "peach-menu", "repo_url": "https://github.com/peachcloud/peach-menu.git"},
    {"name": "peach-buttons", "repo_url": "https://github.com/peachcloud/peach-buttons.git"}
]