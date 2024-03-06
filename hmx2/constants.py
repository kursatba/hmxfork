# ------ Pyth Network ------
DEFAULT_PYTH_PRICE_SERVICE_URL = "https://hermes.pyth.network"

# ------ Contract Address ------
MULTICALL_ADDRESS = "0xcA11bde05977b3631167028862bE2a173976CA11"
CROSS_MARGIN_HANDLER_ADDRESS = "0xB189532c581afB4Fbe69aF6dC3CD36769525d446"
LIMIT_TRADE_HANDLER_ADDRESS = "0xeE116128b9AAAdBcd1f7C18608C5114f594cf5D6"
VAULT_STORAGE_ADDRESS = "0x56CC5A9c0788e674f17F7555dC8D3e2F1C0313C0"
GLP_MANAGER_ADDRESS = "0x3963FfC9dff443c2A94f21b129D429891E32ec18"
PERP_STORAGE_ADDRESS = "0x97e94BdA44a2Df784Ab6535aaE2D62EFC6D2e303"
CONFIG_STORAGE_ADDRESS = "0xF4F7123fFe42c4C90A4bCDD2317D397E0B7d7cc0"
DIX_PRICE_ADAPTER_ADDRESS = "0x222918d230c5A29F334fFb3020aD57b8CeBD1B82"
GM_BTC_PRICE_ADAPTER_ADDRESS = "0x85680bba8a94c9be1DDd7Be802885DFCe95F8164"
GM_ETH_PRICE_ADAPTER_ADDRESS = "0x700083c72eBc86CbFc865830F5706a2DbC392f26"
ONCHAIN_PRICELENS_ADDRESS = "0x7D8eAa8dF02526c711F4ff1f97F6c5324212DBBa"

# ------ ABI Path ------
ERC20_ABI_PATH = "abis/ERC20.json"
CROSS_MARGIN_HANDLER_ABI_PATH = "abis/CrossMarginHandler.json"
LIMIT_TRADE_HANDLER_ABI_PATH = "abis/LimitTradeHandler.json"
VAULT_STORAGE_ABI_PATH = "abis/VaultStorage.json"
GLP_MANAGER_ABI_PATH = "abis/GlpManager.json"
PERP_STORAGE_ABI_PATH = "abis/PerpStorage.json"
CONFIG_STORAGE_ABI_PATH = "abis/ConfigStorage.json"
CIX_PRICE_ADAPTER_ABI_PATH = "abis/CIXPriceAdapter.json"
GM_PRICE_ADAPTER_ABI_PATH = "abis/GMPriceAdapter.json"
ONCHAIN_PRICELENS_ABI_PATH = "abis/OnchainPricelens.json"

# ------ Market ------
MARKET_ETH_USD = 0
MARKET_BTC_USD = 1
MARKET_AAPL_USD = 2
MARKET_JPY_USD = 3
MARKET_XAU_USD = 4
MARKET_AMZN_USD = 5
MARKET_MSFT_USD = 6
MARKET_TSLA_USD = 7
MARKET_EUR_USD = 8
MARKET_XAG_USD = 9
MARKET_AUD_USD = 10
MARKET_GBP_USD = 11
MARKET_ADA_USD = 12
MARKET_MATIC_USD = 13
MARKET_SUI_USD = 14
MARKET_ARB_USD = 15
MARKET_OP_USD = 16
MARKET_LTC_USD = 17
MARKET_COIN_USD = 18
MARKET_GOOG_USD = 19
MARKET_BNB_USD = 20
MARKET_SOL_USD = 21
MARKET_QQQ_USD = 22
MARKET_XRP_USD = 23
MARKET_NVDA_USD = 24
MARKET_LINK_USD = 25
MARKET_USD_CHF = 26
MARKET_DOGE_USD = 27
MARKET_USD_CAD = 28
MARKET_USD_SGD = 29
MARKET_USD_CNH = 30
MARKET_USD_HKD = 31
MARKET_BCH_USD = 32
MARKET_MEME_USD = 33
MARKET_DIX_USD = 34
MARKET_JTO_USD = 35
MARKET_STX_USD = 36
MARKET_ORDI_USD = 37
MARKET_TIA_USD = 38
MARKET_AVAX_USD = 39
MARKET_INJ_USD = 40
MARKET_DOT_USD = 41
MARKET_SEI_USD = 42
MARKET_ATOM_USD = 43
MARKET_PEPE_USD = 44
MARKET_SHIB_USD = 45
MARKET_USD_SEK = 46
MARKET_ICP_USD = 47
MARKET_MANTA_USD = 48
MARKET_STRK_USD = 49
MARKET_PYTH_USD = 50

# ------ Token Profiles ------
TOKEN_PROFILE = {
    "USDC.e": {
        "symbol": "USDC.e",
        "address": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
        "decimals": 6,
    },
    "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8": {
        "symbol": "USDC.e",
        "address": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
        "decimals": 6,
    },
    "USDT": {
        "symbol": "USDT",
        "address": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
        "decimals": 6,
    },
    "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9": {
        "symbol": "USDT",
        "address": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
        "decimals": 6,
    },
    "DAI": {
        "symbol": "DAI",
        "address": "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
        "decimals": 18,
    },
    "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1": {
        "symbol": "DAI",
        "address": "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
        "decimals": 18,
    },
    "WETH": {
        "symbol": "WETH",
        "address": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        "decimals": 18,
    },
    "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1": {
        "symbol": "WETH",
        "address": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        "decimals": 18,
    },
    "WBTC": {
        "symbol": "WBTC",
        "address": "0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f",
        "decimals": 8,
    },
    "0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f": {
        "symbol": "WBTC",
        "address": "0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f",
        "decimals": 8,
    },
    "sGLP": {
        "symbol": "sGLP",
        "address": "0x5402B5F40310bDED796c7D0F3FF6683f5C0cFfdf",
        "decimals": 18,
    },
    "0x5402B5F40310bDED796c7D0F3FF6683f5C0cFfdf": {
        "symbol": "sGLP",
        "address": "0x5402B5F40310bDED796c7D0F3FF6683f5C0cFfdf",
        "decimals": 18,
    },
    "ARB": {
        "symbol": "ARB",
        "address": "0x912CE59144191C1204E64559FE8253a0e49E6548",
        "decimals": 18,
    },
    "0x912CE59144191C1204E64559FE8253a0e49E6548": {
        "symbol": "ARB",
        "address": "0x912CE59144191C1204E64559FE8253a0e49E6548",
        "decimals": 18,
    },
    "wstETH": {
        "symbol": "wstETH",
        "address": "0x5979D7b546E38E414F7E9822514be443A4800529",
        "decimals": 18,
    },
    "0x5979D7b546E38E414F7E9822514be443A4800529": {
        "symbol": "wstETH",
        "address": "0x5979D7b546E38E414F7E9822514be443A4800529",
        "decimals": 18,
    },
    "USDC": {
        "symbol": "USDC",
        "address": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
        "decimals": 6,
    },
    "0xaf88d065e77c8cC2239327C5EDb3A432268e5831": {
        "symbol": "USDC",
        "address": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
        "decimals": 6,
    },
    "gmBTC": {
        "symbol": "gmBTC",
        "address": "0x47c031236e19d024b42f8AE6780E44A573170703",
        "decimals": 18,
    },
    "0x47c031236e19d024b42f8AE6780E44A573170703": {
        "symbol": "gmBTC",
        "address": "0x47c031236e19d024b42f8AE6780E44A573170703",
        "decimals": 18,
    },
    "gmETH": {
        "symbol": "gmETH",
        "address": "0x70d95587d40A2caf56bd97485aB3Eec10Bee6336",
        "decimals": 18,
    },
    "0x70d95587d40A2caf56bd97485aB3Eec10Bee6336": {
        "symbol": "gmETH",
        "address": "0x70d95587d40A2caf56bd97485aB3Eec10Bee6336",
        "decimals": 18,
    },
}

# ------ Collaterals ------
COLLATERAL_USDCe = TOKEN_PROFILE["USDC.e"]["address"]
COLLATERAL_USDT = TOKEN_PROFILE["USDT"]["address"]
COLLATERAL_DAI = TOKEN_PROFILE["DAI"]["address"]
COLLATERAL_WETH = TOKEN_PROFILE["WETH"]["address"]
COLLATERAL_WBTC = TOKEN_PROFILE["WBTC"]["address"]
COLLATERAL_sGLP = TOKEN_PROFILE["sGLP"]["address"]
COLLATERAL_ARB = TOKEN_PROFILE["ARB"]["address"]
COLLATERAL_wstETH = TOKEN_PROFILE["wstETH"]["address"]
COLLATERAL_USDC = TOKEN_PROFILE["USDC"]["address"]
COLLATERAL_gmBTC = TOKEN_PROFILE["gmBTC"]["address"]
COLLATERAL_gmETH = TOKEN_PROFILE["gmETH"]["address"]

COLLATERALS = [
    COLLATERAL_USDCe,
    COLLATERAL_USDT,
    COLLATERAL_DAI,
    COLLATERAL_WETH,
    COLLATERAL_WBTC,
    COLLATERAL_sGLP,
    COLLATERAL_ARB,
    COLLATERAL_wstETH,
    COLLATERAL_USDC,
    COLLATERAL_gmBTC,
    COLLATERAL_gmETH,
]

# ------ Assets ------
ASSET_ETH = "ETH"
ASSET_BTC = "BTC"
ASSET_AAPL = "AAPL"
ASSET_JPY = "JPY"
ASSET_XAU = "XAU"
ASSET_AMZN = "AMZN"
ASSET_MSFT = "MSFT"
ASSET_TSLA = "TSLA"
ASSET_EUR = "EUR"
ASSET_XAG = "XAG"
ASSET_AUD = "AUD"
ASSET_GBP = "GBP"
ASSET_ADA = "ADA"
ASSET_MATIC = "MATIC"
ASSET_SUI = "SUI"
ASSET_ARB = "ARB"
ASSET_OP = "OP"
ASSET_LTC = "LTC"
ASSET_COIN = "COIN"
ASSET_GOOG = "GOOG"
ASSET_BNB = "BNB"
ASSET_SOL = "SOL"
ASSET_QQQ = "QQQ"
ASSET_XRP = "XRP"
ASSET_USDC = "USDC"
ASSET_USDT = "USDT"
ASSET_DAI = "DAI"
ASSET_GLP = "GLP"
ASSET_NVDA = "NVDA"
ASSET_LINK = "LINK"
ASSET_CHF = "CHF"
ASSET_DOGE = "DOGE"
ASSET_CAD = "CAD"
ASSET_SGD = "SGD"
ASSET_CNH = "CNH"
ASSET_wstETH = "wstETH"
ASSET_HKD = "HKD"
ASSET_BCH = "BCH"
ASSET_MEME = "MEME"
ASSET_gmBTC = "gmBTC"
ASSET_gmETH = "gmETH"
ASSET_SEK = "SEK"
ASSET_DIX = "DIX"
ASSET_JTO = "JTO"
ASSET_STX = "STX"
ASSET_ORDI = "ORDI"
ASSET_TIA = "TIA"
ASSET_AVAX = "AVAX"
ASSET_INJ = "INJ"
ASSET_DOT = "DOT"
ASSET_SEI = "SEI"
ASSET_ATOM = "ATOM"
ASSET_PEPE = "1000PEPE"
ASSET_SHIB = "1000SHIB"
ASSET_SEK = "SEK"
ASSET_ICP = "ICP"
ASSET_MANTA = "MANTA"
ASSET_STRK = "STRK"
ASSET_PYTH = "PYTH"

ASSETS = [
    ASSET_ETH,
    ASSET_BTC,
    ASSET_AAPL,
    ASSET_JPY,
    ASSET_XAU,
    ASSET_AMZN,
    ASSET_MSFT,
    ASSET_TSLA,
    ASSET_EUR,
    ASSET_XAG,
    ASSET_AUD,
    ASSET_GBP,
    ASSET_ADA,
    ASSET_MATIC,
    ASSET_SUI,
    ASSET_ARB,
    ASSET_OP,
    ASSET_LTC,
    ASSET_COIN,
    ASSET_GOOG,
    ASSET_BNB,
    ASSET_SOL,
    ASSET_QQQ,
    ASSET_XRP,
    ASSET_USDC,
    ASSET_USDT,
    ASSET_DAI,
    ASSET_GLP,
    ASSET_NVDA,
    ASSET_LINK,
    ASSET_CHF,
    ASSET_DOGE,
    ASSET_CAD,
    ASSET_SGD,
    ASSET_CNH,
    ASSET_wstETH,
    ASSET_HKD,
    ASSET_BCH,
    ASSET_MEME,
    ASSET_gmBTC,
    ASSET_gmETH,
    ASSET_SEK,
    ASSET_DIX,
    ASSET_JTO,
    ASSET_STX,
    ASSET_ORDI,
    ASSET_TIA,
    ASSET_AVAX,
    ASSET_INJ,
    ASSET_DOT,
    ASSET_SEI,
    ASSET_ATOM,
    ASSET_PEPE,
    ASSET_SHIB,
    ASSET_SEK,
    ASSET_ICP,
    ASSET_MANTA,
    ASSET_STRK,
    ASSET_PYTH,
]

# ------ Asset IDs Map ----
COLLATERAL_ASSET_ID_MAP = {
    COLLATERAL_USDCe: ASSET_USDC,
    COLLATERAL_USDT: ASSET_USDT,
    COLLATERAL_DAI: ASSET_DAI,
    COLLATERAL_WETH: ASSET_ETH,
    COLLATERAL_WBTC: ASSET_BTC,
    COLLATERAL_sGLP: ASSET_GLP,
    COLLATERAL_ARB: ASSET_ARB,
    COLLATERAL_wstETH: ASSET_wstETH,
    COLLATERAL_USDC: ASSET_USDC,
    COLLATERAL_gmBTC: ASSET_gmBTC,
    COLLATERAL_gmETH: ASSET_gmETH,
}

# ------ Market ----
MARKET_PROFILE = {
    MARKET_ETH_USD: {"name": "ETHUSD", "asset": ASSET_ETH, "slug": "eth-usd"},
    MARKET_BTC_USD: {"name": "BTCUSD", "asset": ASSET_BTC, "slug": "btc-usd"},
    MARKET_AAPL_USD: {"name": "AAPLUSD", "asset": ASSET_AAPL, "slug": "aapl-usd"},
    MARKET_JPY_USD: {"name": "JPYUSD", "asset": ASSET_JPY, "slug": "jpy-usd"},
    MARKET_XAU_USD: {"name": "XAUUSD", "asset": ASSET_XAU, "slug": "xau-usd"},
    MARKET_AMZN_USD: {"name": "AMZNUSD", "asset": ASSET_AMZN, "slug": "amzn-usd"},
    MARKET_MSFT_USD: {"name": "MSFTUSD", "asset": ASSET_MSFT, "slug": "msft-usd"},
    MARKET_TSLA_USD: {"name": "TSLAUSD", "asset": ASSET_TSLA, "slug": "tsla-usd"},
    MARKET_EUR_USD: {"name": "EURUSD", "asset": ASSET_EUR, "slug": "eur-usd"},
    MARKET_XAG_USD: {"name": "XAGUSD", "asset": ASSET_XAG, "slug": "xag-usd"},
    MARKET_AUD_USD: {"name": "AUDUSD", "asset": ASSET_AUD, "slug": "aud-usd"},
    MARKET_GBP_USD: {"name": "GBPUSD", "asset": ASSET_GBP, "slug": "gbp-usd"},
    MARKET_ADA_USD: {"name": "ADAUSD", "asset": ASSET_ADA, "slug": "ada-usd"},
    MARKET_MATIC_USD: {"name": "MATICUSD", "asset": ASSET_MATIC, "slug": "matic-usd"},
    MARKET_SUI_USD: {"name": "SUIUSD", "asset": ASSET_SUI, "slug": "sui-usd"},
    MARKET_ARB_USD: {"name": "ARBUSD", "asset": ASSET_ARB, "slug": "arb-usd"},
    MARKET_OP_USD: {"name": "OPUSD", "asset": ASSET_OP, "slug": "op-usd"},
    MARKET_LTC_USD: {"name": "LTCUSD", "asset": ASSET_LTC, "slug": "ltc-usd"},
    MARKET_COIN_USD: {"name": "COINUSD", "asset": ASSET_COIN, "slug": "coin-usd"},
    MARKET_GOOG_USD: {"name": "GOOGUSD", "asset": ASSET_GOOG, "slug": "goog-usd"},
    MARKET_BNB_USD: {"name": "BNBUSD", "asset": ASSET_BNB, "slug": "bnb-usd"},
    MARKET_SOL_USD: {"name": "SOLUSD", "asset": ASSET_SOL, "slug": "sol-usd"},
    MARKET_QQQ_USD: {"name": "QQQUSD", "asset": ASSET_QQQ, "slug": "qqq-usd"},
    MARKET_XRP_USD: {"name": "XRPUSD", "asset": ASSET_XRP, "slug": "xrp-usd"},
    MARKET_NVDA_USD: {"name": "NVDAUSD", "asset": ASSET_NVDA, "slug": "nvda-usd"},
    MARKET_LINK_USD: {"name": "LINKUSD", "asset": ASSET_LINK, "slug": "link-usd"},
    MARKET_USD_CHF: {"name": "USDCHF", "asset": ASSET_CHF, "slug": "usd-chf"},
    MARKET_DOGE_USD: {"name": "DOGEUSD", "asset": ASSET_DOGE, "slug": "doge-usd"},
    MARKET_USD_CAD: {"name": "USDCAD", "asset": ASSET_CAD, "slug": "usd-cad"},
    MARKET_USD_SGD: {"name": "USDSGD", "asset": ASSET_SGD, "slug": "usd-sgd"},
    MARKET_USD_CNH: {"name": "USDCNH", "asset": ASSET_CNH, "slug": "usd-cnh"},
    MARKET_USD_HKD: {"name": "USDHKD", "asset": ASSET_HKD, "slug": "usd-hkd"},
    MARKET_BCH_USD: {"name": "BCHUSD", "asset": ASSET_BCH, "slug": "bch-usd"},
    MARKET_MEME_USD: {"name": "MEMEUSD", "asset": ASSET_MEME, "slug": "meme-usd"},
    MARKET_DIX_USD: {"name": "DIXUSD", "asset": ASSET_DIX, "slug": "dix-usd"},
    MARKET_JTO_USD: {"name": "JTOUSD", "asset": ASSET_JTO, "slug": "jto-usd"},
    MARKET_STX_USD: {"name": "STXUSD", "asset": ASSET_STX, "slug": "stx-usd"},
    MARKET_ORDI_USD: {"name": "ORDIUSD", "asset": ASSET_ORDI, "slug": "ordi-usd"},
    MARKET_TIA_USD: {"name": "TIAUSD", "asset": ASSET_TIA, "slug": "tia-usd"},
    MARKET_AVAX_USD: {"name": "AVAXUSD", "asset": ASSET_AVAX, "slug": "avax-usd"},
    MARKET_INJ_USD: {"name": "INJUSD", "asset": ASSET_INJ, "slug": "inj-usd"},
    MARKET_DOT_USD: {"name": "DOTUSD", "asset": ASSET_DOT, "slug": "dot-usd"},
    MARKET_SEI_USD: {"name": "SEIUSD", "asset": ASSET_SEI, "slug": "sei-usd"},
    MARKET_ATOM_USD: {"name": "ATOMUSD", "asset": ASSET_ATOM, "slug": "atom-usd"},
    MARKET_PEPE_USD: {"name": "1000PEPEUSD", "asset": ASSET_PEPE, "slug": "1000pepe-usd"},
    MARKET_SHIB_USD: {"name": "1000SHIBUSD", "asset": ASSET_SHIB, "slug": "1000shib-usd"},
    MARKET_USD_SEK: {"name": "USDSEK", "asset": ASSET_SEK, "slug": "usd-sek"},
    MARKET_ICP_USD: {"name": "ICPUSD", "asset": ASSET_ICP, "slug": "icp-usd"},
    MARKET_MANTA_USD: {"name": "MANTAUSD", "asset": ASSET_MANTA, "slug": "manta-usd"},
    MARKET_STRK_USD: {"name": "STRKUSD", "asset": ASSET_STRK, "slug": "strk-usd"},
    MARKET_PYTH_USD: {"name": "PYTHUSD", "asset": ASSET_PYTH, "slug": "pyth-usd"},
}

# Address
ADDRESS_ZERO = "0x0000000000000000000000000000000000000000"

# Math
MAX_UINT = 2**256 - 1
BPS = 10000

EXECUTION_FEE = 3 * 10**14

SECONDS = 1
MINUTES = 60
HOURS = 3600
DAYS = 86400
YEARS = 31536000
