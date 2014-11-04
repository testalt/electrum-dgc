#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('version', 'lib/util.py')

if sys.version_info[:3] < (2, 6, 0):
    sys.exit("Error: Electrum requires Python version >= 2.6.0...")

usr_share = '/usr/share'
if not os.access(usr_share, os.W_OK):
    usr_share = os.getenv("XDG_DATA_HOME", os.path.join(os.getenv("HOME"), ".local", "share"))

data_files = []
if (len(sys.argv) > 1 and (sys.argv[1] == "sdist")) or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-dgc.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/electrum-dgc.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum.mo' % lang]))


appdata_dir = util.appdata_dir()
if not os.access(appdata_dir, os.W_OK):
    appdata_dir = os.path.join(usr_share, "electrum-dgc")

data_files += [
    (appdata_dir, ["data/README"]),
    (os.path.join(appdata_dir, "cleanlook"), [
        "data/cleanlook/name.cfg",
        "data/cleanlook/style.css"
    ]),
    (os.path.join(appdata_dir, "sahara"), [
        "data/sahara/name.cfg",
        "data/sahara/style.css"
    ]),
    (os.path.join(appdata_dir, "dark"), [
        "data/dark/name.cfg",
        "data/dark/style.css"
    ])
]

for lang in os.listdir('data/wordlist'):
    data_files.append((os.path.join(appdata_dir, 'wordlist'), ['data/wordlist/%s' % lang]))


setup(
    name="Electrum-dgc",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'pyasn1',
        'pyasn1-modules',
        'qrcode',
        'SocksiPy-branch',
        'tlslite'
    ],
    package_dir={
        'electrum_dgc': 'lib',
        'electrum_dgc_gui': 'gui',
        'electrum_dgc_plugins': 'plugins',
    },
    scripts=['electrum-dgc'],
    data_files=data_files,
    py_modules=[
        'electrum_dgc.account',
        'electrum_dgc.bitcoin',
        'electrum_dgc.blockchain',
        'electrum_dgc.bmp',
        'electrum_dgc.commands',
        'electrum_dgc.daemon',
        'electrum_dgc.i18n',
        'electrum_dgc.interface',
        'electrum_dgc.mnemonic',
        'electrum_dgc.msqr',
        'electrum_dgc.network',
        'electrum_dgc.network_proxy',
        'electrum_dgc.old_mnemonic',
        'electrum_dgc.paymentrequest',
        'electrum_dgc.paymentrequest_pb2',
        'electrum_dgc.plugins',
        'electrum_dgc.qrscanner',
        'electrum_dgc.simple_config',
        'electrum_dgc.synchronizer',
        'electrum_dgc.transaction',
        'electrum_dgc.util',
        'electrum_dgc.verifier',
        'electrum_dgc.version',
        'electrum_dgc.wallet',
        'electrum_dgc.x509',
        'electrum_dgcc_gui.gtk',
        'electrum_dgc_gui.qt.__init__',
        'electrum_dgc_gui.qt.amountedit',
        'electrum_dgc_gui.qt.console',
        'electrum_dgc_gui.qt.history_widget',
        'electrum_dgc_gui.qt.icons_rc',
        'electrum_dgc_gui.qt.installwizard',
        'electrum_dgc_gui.qt.lite_window',
        'electrum_dgc_gui.qt.main_window',
        'electrum_dgc_gui.qt.network_dialog',
        'electrum_dgc_gui.qt.password_dialog',
        'electrum_dgc_gui.qt.paytoedit',
        'electrum_dgc_gui.qt.qrcodewidget',
        'electrum_dgc_gui.qt.qrtextedit',
        'electrum_dgc_gui.qt.receiving_widget',
        'electrum_dgc_gui.qt.seed_dialog',
        'electrum_dgc_gui.qt.transaction_dialog',
        'electrum_dgc_gui.qt.util',
        'electrum_dgc_gui.qt.version_getter',
        'electrum_dgc_gui.stdio',
        'electrum_dgc_gui.text',
        'electrum_dgc_plugins.btchipwallet',
        'electrum_dgc_plugins.coinbase_buyback',
        'electrum_dgc_plugins.cosigner_pool',
        'electrum_dgc_plugins.exchange_rate',
        'electrum_dgc_plugins.greenaddress_instant',
        'electrum_dgc_plugins.labels',
        'electrum_dgc_plugins.trezor',
        'electrum_dgc_plugins.virtualkeyboard',
    ],
    description="Lightweight Dogecoin Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU GPLv3",
    url="https://dgc.electrum-alt.org",
    long_description="""Lightweight Dogecoin Wallet"""
)
