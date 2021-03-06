from typing import (
    NamedTuple,
)

from eth.typing import (
    Address,
)
from eth2.beacon.typing import (
    Epoch,
    Gwei,
    Second,
    Shard,
    Slot,
)


Eth2Config = NamedTuple(
    'Eth2Config',
    (
        # Misc
        ('SHARD_COUNT', int),
        ('TARGET_COMMITTEE_SIZE', int),
        ('EJECTION_BALANCE', Gwei),
        ('MAX_BALANCE_CHURN_QUOTIENT', int),
        ('BEACON_CHAIN_SHARD_NUMBER', Shard),
        ('MAX_INDICES_PER_SLASHABLE_VOTE', int),
        ('MAX_EXIT_DEQUEUES_PER_EPOCH', int),
        ('SHUFFLE_ROUND_COUNT', int),
        # State list lengths
        ('SLOTS_PER_HISTORICAL_ROOT', int),
        ('LATEST_ACTIVE_INDEX_ROOTS_LENGTH', int),
        ('LATEST_RANDAO_MIXES_LENGTH', int),
        ('LATEST_SLASHED_EXIT_LENGTH', int),
        # EMPTY_SIGNATURE is defined in constants.py
        # Deposit contract
        ('DEPOSIT_CONTRACT_ADDRESS', Address),
        ('DEPOSIT_CONTRACT_TREE_DEPTH', int),
        ('MIN_DEPOSIT_AMOUNT', Gwei),
        ('MAX_DEPOSIT_AMOUNT', Gwei),
        # ZERO_HASH (ZERO_HASH32) is defined in constants.py
        # Genesis values
        ('GENESIS_FORK_VERSION', int),
        ('GENESIS_SLOT', Slot),
        ('GENESIS_EPOCH', Epoch),
        ('GENESIS_START_SHARD', Shard),
        ('BLS_WITHDRAWAL_PREFIX_BYTE', bytes),
        # Time parameters
        ('SECONDS_PER_SLOT', Second),
        ('MIN_ATTESTATION_INCLUSION_DELAY', int),
        ('SLOTS_PER_EPOCH', int),
        ('MIN_SEED_LOOKAHEAD', int),
        ('ACTIVATION_EXIT_DELAY', int),
        ('EPOCHS_PER_ETH1_VOTING_PERIOD', int),
        ('MIN_VALIDATOR_WITHDRAWABILITY_DELAY', int),
        ('PERSISTENT_COMMITTEE_PERIOD', int),
        # Reward and penalty quotients
        ('BASE_REWARD_QUOTIENT', int),
        ('WHISTLEBLOWER_REWARD_QUOTIENT', int),
        ('ATTESTATION_INCLUSION_REWARD_QUOTIENT', int),
        ('INACTIVITY_PENALTY_QUOTIENT', int),
        ('MIN_PENALTY_QUOTIENT', int),
        # Max operations per block
        ('MAX_PROPOSER_SLASHINGS', int),
        ('MAX_ATTESTER_SLASHINGS', int),
        ('MAX_ATTESTATIONS', int),
        ('MAX_DEPOSITS', int),
        ('MAX_VOLUNTARY_EXITS', int),
        ('MAX_TRANSFERS', int),
    )
)


class CommitteeConfig:
    def __init__(self, config: Eth2Config):
        # Basic
        self.GENESIS_SLOT = config.GENESIS_SLOT
        self.GENESIS_EPOCH = config.GENESIS_EPOCH
        self.SHARD_COUNT = config.SHARD_COUNT
        self.SLOTS_PER_EPOCH = config.SLOTS_PER_EPOCH
        self.TARGET_COMMITTEE_SIZE = config.TARGET_COMMITTEE_SIZE
        self.SHUFFLE_ROUND_COUNT = config.SHUFFLE_ROUND_COUNT

        # For seed
        self.MIN_SEED_LOOKAHEAD = config.MIN_SEED_LOOKAHEAD
        self.ACTIVATION_EXIT_DELAY = config.ACTIVATION_EXIT_DELAY
        self.LATEST_ACTIVE_INDEX_ROOTS_LENGTH = config.LATEST_ACTIVE_INDEX_ROOTS_LENGTH
        self.LATEST_RANDAO_MIXES_LENGTH = config.LATEST_RANDAO_MIXES_LENGTH
