# hltGetConfiguration --cff --data /dev/CMSSW_10_1_0/HIon --type HIon

# /dev/CMSSW_10_1_0/HIon/V78 (CMSSW_10_1_10_HLT1)

import FWCore.ParameterSet.Config as cms

fragment = cms.ProcessFragment( "HLT" )

fragment.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/dev/CMSSW_10_1_0/HIon/V78')
)

fragment.transferSystem = cms.PSet( 
  destinations = cms.vstring( 'Tier0',
    'DQM',
    'ECAL',
    'EventDisplay',
    'Lustre',
    'None' ),
  transferModes = cms.vstring( 'default',
    'test',
    'emulator' ),
  streamA = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'Lustre' )
  ),
  streamCalibration = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamDQM = cms.PSet( 
    default = cms.vstring( 'DQM' ),
    test = cms.vstring( 'DQM',
      'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamDQMCalibration = cms.PSet( 
    default = cms.vstring( 'DQM' ),
    test = cms.vstring( 'DQM',
      'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamEcalCalibration = cms.PSet( 
    default = cms.vstring( 'ECAL' ),
    test = cms.vstring( 'ECAL' ),
    emulator = cms.vstring( 'None' )
  ),
  streamEventDisplay = cms.PSet( 
    default = cms.vstring( 'EventDisplay',
      'Tier0' ),
    test = cms.vstring( 'EventDisplay',
      'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamExpressCosmics = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'Lustre' )
  ),
  streamNanoDST = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamRPCMON = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamTrackerCalibration = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  default = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'Lustre' ),
    streamLookArea = cms.PSet(  )
  ),
  streamLookArea = cms.PSet( 
    default = cms.vstring( 'DQM' ),
    test = cms.vstring( 'DQM',
      'Lustre' ),
    emulator = cms.vstring( 'None' )
  )
)
fragment.HLTPSetInitialCkfTrajectoryFilterForHI = cms.PSet( 
  minimumNumberOfHits = cms.int32( 6 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.9 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 999 )
)
fragment.HLTIter0PSetTrajectoryBuilderIT = cms.PSet( 
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  lostHitPenalty = cms.double( 30.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  maxCand = cms.int32( 2 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  intermediateCleaning = cms.bool( True ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTIter4PSetTrajectoryBuilderIT = cms.PSet( 
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltIter4ESPMeasurementTracker" ),
  lostHitPenalty = cms.double( 30.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter4PSetTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.untracked.int32( 4 ),
  maxCand = cms.int32( 1 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  intermediateCleaning = cms.bool( True ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTPSetTobTecStepInOutTrajectoryFilterBase = cms.PSet( 
  minimumNumberOfHits = cms.int32( 4 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.1 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedPairPenalty = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 0 )
)
fragment.HLTIter0GroupedCkfTrajectoryBuilderIT = cms.PSet( 
  keepOriginalIfRebuildFails = cms.bool( False ),
  lockHits = cms.bool( True ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryFilterIT" ) ),
  doSeedingRegionRebuilding = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  maxCand = cms.int32( 2 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  intermediateCleaning = cms.bool( True ),
  bestHitOnly = cms.bool( True ),
  useSameTrajFilter = cms.bool( True ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  lostHitPenalty = cms.double( 30.0 ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( False ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryFilterIT" ) ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTSiStripClusterChargeCutTiny = cms.PSet(  value = cms.double( 800.0 ) )
fragment.HLTPSetTrajectoryFilterIT = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTIter4PSetTrajectoryFilterIT = cms.PSet( 
  minimumNumberOfHits = cms.int32( 6 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 0 )
)
fragment.HLTPSetTrajectoryBuilderForElectrons = cms.PSet( 
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  lostHitPenalty = cms.double( 90.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "hltESPBwdElectronPropagator" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterForElectrons" ) ),
  propagatorAlong = cms.string( "hltESPFwdElectronPropagator" ),
  maxCand = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  intermediateCleaning = cms.bool( False ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTPSetPvClusterComparerForIT = cms.PSet( 
  track_chi2_max = cms.double( 20.0 ),
  track_pt_max = cms.double( 20.0 ),
  track_prob_min = cms.double( -1.0 ),
  track_pt_min = cms.double( 1.0 )
)
fragment.HLTPSetMixedStepTrajectoryFilter = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.1 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.4 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 999 )
)
fragment.HLTPSetInitialCkfTrajectoryBuilderForHI = cms.PSet( 
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  lostHitPenalty = cms.double( 30.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialCkfTrajectoryFilterForHI" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  maxCand = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  intermediateCleaning = cms.bool( False ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet( 
  rescaleErrorIfFail = cms.double( 1.0 ),
  ComponentType = cms.string( "MuonCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  lostHitPenalty = cms.double( 30.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryFilter" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  maxCand = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  intermediateCleaning = cms.bool( False ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  deltaEta = cms.double( -1.0 ),
  useSeedLayer = cms.bool( False ),
  deltaPhi = cms.double( -1.0 )
)
fragment.HLTIter0HighPtTkMuPSetTrajectoryFilterIT = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTPSetPvClusterComparerForBTag = cms.PSet( 
  track_chi2_max = cms.double( 20.0 ),
  track_pt_max = cms.double( 20.0 ),
  track_prob_min = cms.double( -1.0 ),
  track_pt_min = cms.double( 0.1 )
)
fragment.HLTSeedFromConsecutiveHitsTripletOnlyCreator = cms.PSet( 
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  forceKinematicWithRegionDirection = cms.bool( False ),
  magneticField = cms.string( "ParabolicMf" ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  ComponentName = cms.string( "SeedFromConsecutiveHitsTripletOnlyCreator" ),
  MinOneOverPtError = cms.double( 1.0 )
)
fragment.HLTIter2GroupedCkfTrajectoryBuilderIT = cms.PSet( 
  keepOriginalIfRebuildFails = cms.bool( False ),
  lockHits = cms.bool( True ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryFilterIT" ) ),
  doSeedingRegionRebuilding = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  maxCand = cms.int32( 2 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  intermediateCleaning = cms.bool( True ),
  bestHitOnly = cms.bool( True ),
  useSameTrajFilter = cms.bool( True ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  lostHitPenalty = cms.double( 30.0 ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( False ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryFilterIT" ) ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTIter3PSetTrajectoryBuilderIT = cms.PSet( 
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltIter3ESPMeasurementTracker" ),
  lostHitPenalty = cms.double( 30.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter3PSetTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  maxCand = cms.int32( 1 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  intermediateCleaning = cms.bool( True ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTSiStripClusterChargeCutTight = cms.PSet(  value = cms.double( 1945.0 ) )
fragment.HLTPSetCkf3HitTrajectoryFilter = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.9 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( -1 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTPSetDetachedStepTrajectoryFilterBase = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 2 ),
  minPt = cms.double( 0.075 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 999 )
)
fragment.HLTPSetMuonTrackingRegionBuilder8356 = cms.PSet( 
  Rescale_Dz = cms.double( 3.0 ),
  Pt_fixed = cms.bool( False ),
  Eta_fixed = cms.bool( False ),
  Eta_min = cms.double( 0.1 ),
  DeltaZ = cms.double( 15.9 ),
  maxRegions = cms.int32( 2 ),
  EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
  UseVertex = cms.bool( False ),
  Z_fixed = cms.bool( True ),
  PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
  PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
  Rescale_phi = cms.double( 3.0 ),
  DeltaEta = cms.double( 0.2 ),
  precise = cms.bool( True ),
  OnDemand = cms.int32( -1 ),
  EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
  MeasurementTrackerName = cms.InputTag( "hltESPMeasurementTracker" ),
  vertexCollection = cms.InputTag( "pixelVertices" ),
  Pt_min = cms.double( 1.5 ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  Phi_fixed = cms.bool( False ),
  DeltaR = cms.double( 0.2 ),
  input = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
  DeltaPhi = cms.double( 0.2 ),
  Phi_min = cms.double( 0.1 ),
  Rescale_eta = cms.double( 3.0 )
)
fragment.HLTPSetDetachedCkfTrajectoryFilterForHI = cms.PSet( 
  minimumNumberOfHits = cms.int32( 6 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 0.701 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTIter3PSetTrajectoryFilterIT = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 0 )
)
fragment.HLTPSetJetCoreStepTrajectoryFilter = cms.PSet( 
  minimumNumberOfHits = cms.int32( 4 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.1 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 999 )
)
fragment.HLTIter2PSetTrajectoryFilterIT = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 0 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  lostHitPenalty = cms.double( 30.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuTrackJpsiTrajectoryFilter" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  maxCand = cms.int32( 1 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  intermediateCleaning = cms.bool( True ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTPSetTrajectoryBuilderForGsfElectrons = cms.PSet( 
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  lostHitPenalty = cms.double( 90.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "hltESPBwdElectronPropagator" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterForElectrons" ) ),
  propagatorAlong = cms.string( "hltESPFwdElectronPropagator" ),
  maxCand = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator2000" ),
  intermediateCleaning = cms.bool( False ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTSiStripClusterChargeCutNone = cms.PSet(  value = cms.double( -1.0 ) )
fragment.HLTPSetTobTecStepTrajectoryFilterBase = cms.PSet( 
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.1 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedPairPenalty = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 0 )
)
fragment.HLTPSetMuonCkfTrajectoryFilter = cms.PSet( 
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.9 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( -1 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTPSetbJetRegionalTrajectoryFilter = cms.PSet( 
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 1.0 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 8 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTPSetDetachedStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CompositeTrajectoryFilter" ),
  filters = cms.VPSet( 
    cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedStepTrajectoryFilterBase" )    )
  )
)
fragment.HLTIter1PSetTrajectoryFilterIT = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 0 ),
  minPt = cms.double( 0.2 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet( 
  minimumNumberOfHits = cms.int32( 6 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 8.0 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 0.701 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTPSetMixedStepTrajectoryBuilder = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialForMixedStepOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMixedStepTrajectoryFilter" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForMixedStep" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 2 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeTightMeasurementEstimator16" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMixedStepTrajectoryFilter" ) ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTPSetMixedStepTrajectoryFilterBase = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.05 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 0 )
)
fragment.HLTPSetCkfTrajectoryFilter = cms.PSet( 
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.9 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( -1 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTSeedFromProtoTracks = cms.PSet( 
  TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  forceKinematicWithRegionDirection = cms.bool( False ),
  magneticField = cms.string( "ParabolicMf" ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  MinOneOverPtError = cms.double( 1.0 )
)
fragment.HLTPSetInitialStepTrajectoryFilterBase = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 2 ),
  minPt = cms.double( 0.2 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 999 )
)
fragment.HLTIter2PSetTrajectoryBuilderIT = cms.PSet( 
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltIter2ESPMeasurementTracker" ),
  lostHitPenalty = cms.double( 30.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  maxCand = cms.int32( 2 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  intermediateCleaning = cms.bool( True ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet( 
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 10.0 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 8 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTSeedFromConsecutiveHitsCreatorIT = cms.PSet( 
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  forceKinematicWithRegionDirection = cms.bool( False ),
  magneticField = cms.string( "ParabolicMf" ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  MinOneOverPtError = cms.double( 1.0 )
)
fragment.HLTPSetTrajectoryFilterL3 = cms.PSet( 
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.5 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 1000000000 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTPSetDetachedStepTrajectoryBuilder = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedStepTrajectoryFilter" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 3 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedStepTrajectoryFilter" ) ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet( 
  minimumNumberOfHits = cms.int32( 6 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 8.0 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 100 )
)
fragment.HLTIter0PSetTrajectoryFilterIT = cms.PSet( 
  minimumNumberOfHits = cms.int32( 4 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 0 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTIter2HighPtTkMuPSetTrajectoryFilterIT = cms.PSet( 
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 3 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTPSetMuTrackJpsiEffTrajectoryFilter = cms.PSet( 
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 1.0 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 9 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTPSetPixelPairCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 3 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9ForHI" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8" ) ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTSiStripClusterChargeCutLoose = cms.PSet(  value = cms.double( 1620.0 ) )
fragment.HLTPSetPixelPairStepTrajectoryFilterBase = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 2 ),
  minPt = cms.double( 0.1 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 999 )
)
fragment.HLTPSetLowPtStepTrajectoryFilter = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 1 ),
  minPt = cms.double( 0.075 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 999 )
)
fragment.HLTSeedFromConsecutiveHitsCreator = cms.PSet( 
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  propagator = cms.string( "PropagatorWithMaterial" ),
  forceKinematicWithRegionDirection = cms.bool( False ),
  magneticField = cms.string( "" ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  MinOneOverPtError = cms.double( 1.0 )
)
fragment.HLTPSetPixelPairCkfTrajectoryBuilderForHI = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHI" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 3 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9ForHI" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHI" ) ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTPSetDetachedCkfTrajectoryBuilderForHI = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  maxDPhiForLooperReconstruction = cms.double( 0.0 ),
  maxPtForLooperReconstruction = cms.double( 0.0 ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHI" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 2 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHI" ) ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTIter1PSetTrajectoryBuilderIT = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTracker" ),
  lostHitPenalty = cms.double( 30.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  maxCand = cms.int32( 2 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  intermediateCleaning = cms.bool( True ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTPSetDetachedCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  maxDPhiForLooperReconstruction = cms.double( 0.0 ),
  maxPtForLooperReconstruction = cms.double( 0.0 ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 2 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8" ) ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTSiStripClusterChargeCutForHI = cms.PSet(  value = cms.double( 2069.0 ) )
fragment.HLTPSetLowPtStepTrajectoryBuilder = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtStepTrajectoryFilter" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 4 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtStepTrajectoryFilter" ) ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTPSetMuTrackJpsiEffTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  lostHitPenalty = cms.double( 30.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuTrackJpsiEffTrajectoryFilter" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  maxCand = cms.int32( 1 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  intermediateCleaning = cms.bool( True ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTPSetTrajectoryFilterForElectrons = cms.PSet( 
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 2.0 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( -1 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( -1 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTPSetJetCoreStepTrajectoryBuilder = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetJetCoreStepTrajectoryFilter" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 50 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetJetCoreStepTrajectoryFilter" ) ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTPSetPvClusterComparer = cms.PSet( 
  track_chi2_max = cms.double( 9999999.0 ),
  track_pt_max = cms.double( 10.0 ),
  track_prob_min = cms.double( -1.0 ),
  track_pt_min = cms.double( 2.5 )
)
fragment.HLTIter0HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet( 
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  lostHitPenalty = cms.double( 30.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0HighPtTkMuPSetTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  maxCand = cms.int32( 4 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  intermediateCleaning = cms.bool( True ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTPSetPixelLessStepTrajectoryFilterBase = cms.PSet( 
  minimumNumberOfHits = cms.int32( 4 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.05 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 0 )
)
fragment.HLTIter1GroupedCkfTrajectoryBuilderIT = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTracker" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 2 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTPSetMuonCkfTrajectoryBuilderSeedHit = cms.PSet( 
  rescaleErrorIfFail = cms.double( 1.0 ),
  ComponentType = cms.string( "MuonCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  lostHitPenalty = cms.double( 30.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryFilter" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  maxCand = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  intermediateCleaning = cms.bool( False ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  deltaEta = cms.double( -1.0 ),
  useSeedLayer = cms.bool( True ),
  deltaPhi = cms.double( -1.0 )
)
fragment.HLTPSetPixelPairCkfTrajectoryFilterForHI = cms.PSet( 
  minimumNumberOfHits = cms.int32( 6 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 1.0 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 100 )
)
fragment.HLTPSetInitialStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 3 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  foundHitBonus = cms.double( 10.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( True ),
  estimator = cms.string( "hltESPInitialStepChi2ChargeMeasurementEstimator30" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 1 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
fragment.HLTPSetInitialStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.2 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  pixelSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) )
)
fragment.HLTPSetLowPtQuadStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtQuadStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtQuadStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 4 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  foundHitBonus = cms.double( 10.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
fragment.HLTPSetLowPtQuadStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.075 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  pixelSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) )
)
fragment.HLTPSetHighPtTripletStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetHighPtTripletStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetHighPtTripletStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 3 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  foundHitBonus = cms.double( 10.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
fragment.HLTPSetHighPtTripletStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  seedPairPenalty = cms.int32( 5 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.2 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  pixelSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) )
)
fragment.HLTPSetLowPtTripletStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtTripletStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtTripletStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 4 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  foundHitBonus = cms.double( 10.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
fragment.HLTPSetLowPtTripletStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.075 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  pixelSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) )
)
fragment.HLTPSetDetachedQuadStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedQuadStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedQuadStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 3 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  foundHitBonus = cms.double( 10.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
fragment.HLTPSetDetachedQuadStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.075 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  pixelSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) )
)
fragment.HLTPSetDetachedTripletStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedTripletStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedTripletStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 3 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  foundHitBonus = cms.double( 10.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
fragment.HLTPSetDetachedTripletStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.075 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  pixelSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) )
)
fragment.HLTPSetMixedTripletStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForMixedStep" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMixedTripletStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMixedTripletStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 2 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  foundHitBonus = cms.double( 10.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPMixedTripletStepChi2ChargeMeasurementEstimator16" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialForMixedStepOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
fragment.HLTPSetMixedTripletStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.4 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  pixelSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
)
fragment.HLTPSetPixelLessStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelLessStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelLessStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 2 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  foundHitBonus = cms.double( 10.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPPixelLessStepChi2ChargeMeasurementEstimator16" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 4 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
fragment.HLTPSetPixelLessStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 4 ),
  seedPairPenalty = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 0 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  pixelSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
)
fragment.HLTPSetTobTecStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 5 ),
  seedPairPenalty = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 0 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  pixelSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
)
fragment.HLTPSetTobTecStepInOutTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 4 ),
  seedPairPenalty = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 0 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  pixelSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
)
fragment.HLTPSetTobTecStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTobTecStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTobTecStepInOutTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( False ),
  maxCand = cms.int32( 2 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  foundHitBonus = cms.double( 10.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPTobTecStepChi2ChargeMeasurementEstimator16" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 4 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
fragment.HLTPSetGroupedCkfTrajectoryBuilderIterL3ForOI = cms.PSet( 
  rescaleErrorIfFail = cms.double( 1.0 ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lockHits = cms.bool( True ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetCkfTrajectoryFilterIterL3OI" ) ),
  maxCand = cms.int32( 5 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  intermediateCleaning = cms.bool( True ),
  bestHitOnly = cms.bool( True ),
  deltaEta = cms.double( -1.0 ),
  useSeedLayer = cms.bool( False ),
  useSameTrajFilter = cms.bool( True ),
  MeasurementTrackerName = cms.string( "hltSiStripClusters" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  lostHitPenalty = cms.double( 30.0 ),
  requireSeedHitsInRebuild = cms.bool( False ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( True ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetCkfTrajectoryFilterIterL3OI" ) ),
  foundHitBonus = cms.double( 1000.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  deltaPhi = cms.double( -1.0 )
)
fragment.HLTIter0IterL3MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "" ),
  keepOriginalIfRebuildFails = cms.bool( True ),
  lostHitPenalty = cms.double( 1.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  minNrOfHitsForRebuild = cms.int32( 2 ),
  maxCand = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT" ) ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 1000.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.9 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 10.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 999 )
)
fragment.HLTIter0IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "" ),
  keepOriginalIfRebuildFails = cms.bool( True ),
  lostHitPenalty = cms.double( 1.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  minNrOfHitsForRebuild = cms.int32( 2 ),
  maxCand = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT" ) ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 1000.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT = cms.PSet( 
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.9 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 10.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 999 )
)
fragment.HLTIter2HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet( 
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltIter2HighPtTkMuESPMeasurementTracker" ),
  lostHitPenalty = cms.double( 30.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2HighPtTkMuPSetTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  maxCand = cms.int32( 2 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  intermediateCleaning = cms.bool( True ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT = cms.PSet( 
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 3 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTIter2IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltIter2HighPtTkMuESPMeasurementTracker" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( False ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 2 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 1000.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTIter2IterL3MuonPSetTrajectoryFilterIT = cms.PSet( 
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 3 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTIter2IterL3MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet( 
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltIter2HighPtTkMuESPMeasurementTracker" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( False ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2IterL3MuonPSetTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 2 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 1000.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTPSetCkfTrajectoryFilterIterL3OI = cms.PSet( 
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 3.0 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 10.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( -1 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTPSetPixelPairStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 4 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  pixelSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) )
)
fragment.HLTPSetPixelPairStepTrajectoryFilterInOut = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 4 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 1 ),
  strictSeedExtension = cms.bool( False ),
  pixelSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) )
)
fragment.HLTPSetPixelPairStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairStepTrajectoryFilterInOut" ) ),
  useSameTrajFilter = cms.bool( False ),
  maxCand = cms.int32( 3 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  foundHitBonus = cms.double( 10.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPPixelPairStepChi2ChargeMeasurementEstimator9" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
fragment.streams = cms.PSet( 
  DQM = cms.vstring( 'OnlineMonitor' ),
  PhysicsCommissioning = cms.vstring( 'HLTPhysics',
    'ZeroBias' )
)
fragment.datasets = cms.PSet( 
  HLTPhysics = cms.vstring( 'HLT_Physics_v7' ),
  OnlineMonitor = cms.vstring( 'HLT_Physics_v7',
    'HLT_Random_v3',
    'HLT_ZeroBias_v6' ),
  ZeroBias = cms.vstring( 'HLT_Random_v3',
    'HLT_ZeroBias_v6' )
)

fragment.CSCChannelMapperESSource = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "CSCChannelMapperRecord" ),
    firstValid = cms.vuint32( 1 )
)
fragment.CSCINdexerESSource = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "CSCIndexerRecord" ),
    firstValid = cms.vuint32( 1 )
)
fragment.GlobalParametersRcdSource = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "L1TGlobalParametersRcd" ),
    firstValid = cms.vuint32( 1 )
)
fragment.HcalTimeSlewEP = cms.ESSource( "HcalTimeSlewEP",
    timeSlewParametersM3 = cms.VPSet( 
      cms.PSet(  tspar2 = cms.double( 0.0 ),
        tspar0 = cms.double( 12.2999 ),
        tspar1 = cms.double( -2.19142 ),
        tspar1_siPM = cms.double( 0.0 ),
        cap = cms.double( 6.0 ),
        tspar0_siPM = cms.double( 0.0 ),
        tspar2_siPM = cms.double( 0.0 )
      ),
      cms.PSet(  tspar2 = cms.double( 32.0 ),
        tspar0 = cms.double( 15.5 ),
        tspar1 = cms.double( -3.2 ),
        tspar1_siPM = cms.double( 0.0 ),
        cap = cms.double( 6.0 ),
        tspar0_siPM = cms.double( 0.0 ),
        tspar2_siPM = cms.double( 0.0 )
      ),
      cms.PSet(  tspar2 = cms.double( 0.0 ),
        tspar0 = cms.double( 12.2999 ),
        tspar1 = cms.double( -2.19142 ),
        tspar1_siPM = cms.double( 0.0 ),
        cap = cms.double( 6.0 ),
        tspar0_siPM = cms.double( 0.0 ),
        tspar2_siPM = cms.double( 0.0 )
      ),
      cms.PSet(  tspar2 = cms.double( 0.0 ),
        tspar0 = cms.double( 12.2999 ),
        tspar1 = cms.double( -2.19142 ),
        tspar1_siPM = cms.double( 0.0 ),
        cap = cms.double( 6.0 ),
        tspar0_siPM = cms.double( 0.0 ),
        tspar2_siPM = cms.double( 0.0 )
      )
    ),
    timeSlewParametersM2 = cms.VPSet( 
      cms.PSet(  slope = cms.double( -3.178648 ),
        tmax = cms.double( 16.0 ),
        tzero = cms.double( 23.960177 )
      ),
      cms.PSet(  slope = cms.double( -1.5610227 ),
        tmax = cms.double( 10.0 ),
        tzero = cms.double( 11.977461 )
      ),
      cms.PSet(  slope = cms.double( -1.075824 ),
        tmax = cms.double( 6.25 ),
        tzero = cms.double( 9.109694 )
      )
    ),
    appendToDataLabel = cms.string( "HBHE" )
)
fragment.hltESSBTagRecord = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "JetTagComputerRecord" ),
    firstValid = cms.vuint32( 1 )
)
fragment.hltESSEcalSeverityLevel = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "EcalSeverityLevelAlgoRcd" ),
    firstValid = cms.vuint32( 1 )
)
fragment.hltESSHcalSeverityLevel = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "HcalSeverityLevelComputerRcd" ),
    firstValid = cms.vuint32( 1 )
)

fragment.hltBoostedDoubleSecondaryVertexAK8Computer = cms.ESProducer( "CandidateBoostedDoubleSecondaryVertexESProducer",
  weightFile = cms.FileInPath( "RecoBTag/SecondaryVertex/data/BoostedDoubleSV_AK8_BDT_v4.weights.xml.gz" ),
  useCondDB = cms.bool( False ),
  useGBRForest = cms.bool( True ),
  useAdaBoost = cms.bool( False )
)
fragment.AnyDirectionAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "AnyDirectionAnalyticalPropagator" ),
  PropagationDirection = cms.string( "anyDirection" )
)
fragment.CSCChannelMapperESProducer = cms.ESProducer( "CSCChannelMapperESProducer",
  AlgoName = cms.string( "CSCChannelMapperPostls1" )
)
fragment.CSCIndexerESProducer = cms.ESProducer( "CSCIndexerESProducer",
  AlgoName = cms.string( "CSCIndexerPostls1" )
)
fragment.CSCObjectMapESProducer = cms.ESProducer( "CSCObjectMapESProducer",
  appendToDataLabel = cms.string( "" )
)
fragment.CaloTopologyBuilder = cms.ESProducer( "CaloTopologyBuilder" )
fragment.CaloTowerConstituentsMapBuilder = cms.ESProducer( "CaloTowerConstituentsMapBuilder",
  appendToDataLabel = cms.string( "" ),
  MapAuto = cms.untracked.bool( False ),
  SkipHE = cms.untracked.bool( False ),
  MapFile = cms.untracked.string( "Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz" )
)
fragment.CaloTowerTopologyEP = cms.ESProducer( "CaloTowerTopologyEP",
  appendToDataLabel = cms.string( "" )
)
fragment.CastorDbProducer = cms.ESProducer( "CastorDbProducer",
  appendToDataLabel = cms.string( "" )
)
fragment.ClusterShapeHitFilterESProducer = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "ClusterShapeHitFilter" ),
  PixelShapeFileL1 = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par" )
)
fragment.DTObjectMapESProducer = cms.ESProducer( "DTObjectMapESProducer",
  appendToDataLabel = cms.string( "" )
)
fragment.GlobalParameters = cms.ESProducer( "StableParametersTrivialProducer",
  NumberL1JetCounts = cms.uint32( 12 ),
  NumberL1NoIsoEG = cms.uint32( 4 ),
  NumberL1CenJet = cms.uint32( 4 ),
  NumberL1Tau = cms.uint32( 12 ),
  NumberConditionChips = cms.uint32( 1 ),
  NumberL1EGamma = cms.uint32( 12 ),
  TotalBxInEvent = cms.int32( 5 ),
  NumberL1Mu = cms.uint32( 4 ),
  PinsOnConditionChip = cms.uint32( 512 ),
  WordLength = cms.int32( 64 ),
  PinsOnChip = cms.uint32( 512 ),
  OrderOfChip = cms.vint32( 1 ),
  IfMuEtaNumberBits = cms.uint32( 6 ),
  OrderConditionChip = cms.vint32( 1 ),
  appendToDataLabel = cms.string( "" ),
  NumberL1TauJet = cms.uint32( 4 ),
  NumberL1Jet = cms.uint32( 12 ),
  NumberPhysTriggers = cms.uint32( 512 ),
  NumberL1Muon = cms.uint32( 8 ),
  UnitLength = cms.int32( 8 ),
  NumberL1IsoEG = cms.uint32( 4 ),
  NumberTechnicalTriggers = cms.uint32( 64 ),
  NumberL1ForJet = cms.uint32( 4 ),
  IfCaloEtaNumberBits = cms.uint32( 4 ),
  NumberPsbBoards = cms.int32( 7 ),
  NumberChips = cms.uint32( 1 ),
  NumberPhysTriggersExtended = cms.uint32( 64 )
)
fragment.MaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterial" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.MaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.MaterialPropagatorParabolicMF = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialParabolicMf" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.OppositeMaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.OppositeMaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.OppositeMaterialPropagatorParabolicMF = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.OppositePropagatorWithMaterialForMixedStep = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForMixedStepOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( 0.1 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.PropagatorWithMaterialForLoopers = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForLoopers" ),
  Mass = cms.double( 0.1396 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 4.0 ),
  useRungeKutta = cms.bool( False )
)
fragment.PropagatorWithMaterialForMixedStep = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForMixedStep" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( 0.1 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.SiStripRegionConnectivity = cms.ESProducer( "SiStripRegionConnectivity",
  EtaDivisions = cms.untracked.uint32( 20 ),
  PhiDivisions = cms.untracked.uint32( 20 ),
  EtaMax = cms.untracked.double( 2.5 )
)
fragment.SimpleSecondaryVertex3TrkComputer = cms.ESProducer( "SimpleSecondaryVertexESProducer",
  minTracks = cms.uint32( 3 ),
  minVertices = cms.uint32( 1 ),
  use3d = cms.bool( True ),
  unBoost = cms.bool( False ),
  useSignificance = cms.bool( True )
)
fragment.SteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "SteppingHelixPropagatorAny" )
)
fragment.TransientTrackBuilderESProducer = cms.ESProducer( "TransientTrackBuilderESProducer",
  ComponentName = cms.string( "TransientTrackBuilder" )
)
fragment.caloDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "CaloDetIdAssociator" ),
  hcalRegion = cms.int32( 2 ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False ),
  includeME0 = cms.bool( False ),
  includeGEM = cms.bool( False )
)
fragment.cosmicsNavigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "CosmicNavigationSchool" ),
  SimpleMagneticField = cms.string( "" )
)
fragment.ecalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "EcalDetIdAssociator" ),
  hcalRegion = cms.int32( 2 ),
  etaBinSize = cms.double( 0.02 ),
  nEta = cms.int32( 300 ),
  nPhi = cms.int32( 360 ),
  includeBadChambers = cms.bool( False ),
  includeME0 = cms.bool( False ),
  includeGEM = cms.bool( False )
)
fragment.ecalSeverityLevel = cms.ESProducer( "EcalSeverityLevelESProducer",
  dbstatusMask = cms.PSet( 
    kBad = cms.vstring( 'kNonRespondingIsolated',
      'kDeadVFE',
      'kDeadFE',
      'kNoDataNoTP' ),
    kGood = cms.vstring( 'kOk' ),
    kRecovered = cms.vstring(  ),
    kProblematic = cms.vstring( 'kDAC',
      'kNoLaser',
      'kNoisy',
      'kNNoisy',
      'kNNNoisy',
      'kNNNNoisy',
      'kNNNNNoisy',
      'kFixedG6',
      'kFixedG1',
      'kFixedG0' ),
    kWeird = cms.vstring(  ),
    kTime = cms.vstring(  )
  ),
  timeThresh = cms.double( 2.0 ),
  flagMask = cms.PSet( 
    kBad = cms.vstring( 'kFaultyHardware',
      'kDead',
      'kKilled' ),
    kGood = cms.vstring( 'kGood' ),
    kRecovered = cms.vstring( 'kLeadingEdgeRecovered',
      'kTowerRecovered' ),
    kProblematic = cms.vstring( 'kPoorReco',
      'kPoorCalib',
      'kNoisy',
      'kSaturated' ),
    kWeird = cms.vstring( 'kWeird',
      'kDiWeird' ),
    kTime = cms.vstring( 'kOutOfTime' )
  )
)
fragment.hcalDDDRecConstants = cms.ESProducer( "HcalDDDRecConstantsESModule",
  appendToDataLabel = cms.string( "" )
)
fragment.hcalDDDSimConstants = cms.ESProducer( "HcalDDDSimConstantsESModule",
  appendToDataLabel = cms.string( "" )
)
fragment.hcalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HcalDetIdAssociator" ),
  hcalRegion = cms.int32( 2 ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False ),
  includeME0 = cms.bool( False ),
  includeGEM = cms.bool( False )
)
fragment.hcalRecAlgos = cms.ESProducer( "HcalRecAlgoESProducer",
  phase = cms.uint32( 1 ),
  RecoveredRecHitBits = cms.vstring(  ),
  appendToDataLabel = cms.string( "" ),
  SeverityLevels = cms.VPSet( 
    cms.PSet(  ChannelStatus = cms.vstring(  ),
      RecHitFlags = cms.vstring( 'TimingFromTDC' ),
      Level = cms.int32( 0 )
    ),
    cms.PSet(  ChannelStatus = cms.vstring( 'HcalCellCaloTowerProb' ),
      RecHitFlags = cms.vstring(  ),
      Level = cms.int32( 1 )
    ),
    cms.PSet(  ChannelStatus = cms.vstring( 'HcalCellExcludeFromHBHENoiseSummary' ),
      RecHitFlags = cms.vstring(  ),
      Level = cms.int32( 5 )
    ),
    cms.PSet(  ChannelStatus = cms.vstring(  ),
      RecHitFlags = cms.vstring( 'HBHEHpdHitMultiplicity',
        'HBHEIsolatedNoise',
        'HBHEFlatNoise',
        'HBHESpikeNoise',
        'HBHETS4TS5Noise',
        'HBHENegativeNoise',
        'HBHEPulseFitBit',
        'HBHEOOTPU' ),
      Level = cms.int32( 8 )
    ),
    cms.PSet(  ChannelStatus = cms.vstring(  ),
      RecHitFlags = cms.vstring( 'HFLongShort',
        'HFS8S1Ratio',
        'HFPET',
        'HFSignalAsymmetry' ),
      Level = cms.int32( 11 )
    ),
    cms.PSet(  ChannelStatus = cms.vstring( 'HcalCellHot' ),
      RecHitFlags = cms.vstring(  ),
      Level = cms.int32( 15 )
    ),
    cms.PSet(  ChannelStatus = cms.vstring( 'HcalCellOff',
  'HcalCellDead' ),
      RecHitFlags = cms.vstring(  ),
      Level = cms.int32( 20 )
    )
  ),
  DropChannelStatusBits = cms.vstring( 'HcalCellMask',
    'HcalCellOff',
    'HcalCellDead' )
)
fragment.hltCombinedSecondaryVertex = cms.ESProducer( "CombinedSecondaryVertexESProducer",
  recordLabel = cms.string( "HLT" ),
  categoryVariableName = cms.string( "vertexCategory" ),
  useTrackWeights = cms.bool( True ),
  useCategories = cms.bool( True ),
  pseudoMultiplicityMin = cms.uint32( 2 ),
  correctVertexMass = cms.bool( True ),
  trackSelection = cms.PSet( 
    maxDistToAxis = cms.double( 0.07 ),
    totalHitsMin = cms.uint32( 0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dValMax = cms.double( 99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    qualityClass = cms.string( "any" ),
    jetDeltaRMax = cms.double( 0.3 ),
    normChi2Max = cms.double( 99999.9 ),
    pixelHitsMin = cms.uint32( 0 ),
    sip2dSigMin = cms.double( -99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  calibrationRecords = cms.vstring( 'CombinedSVRecoVertex',
    'CombinedSVPseudoVertex',
    'CombinedSVNoVertex' ),
  trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
  charmCut = cms.double( 1.5 ),
  vertexFlip = cms.bool( False ),
  minimumTrackWeight = cms.double( 0.5 ),
  pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
  trackMultiplicityMin = cms.uint32( 3 ),
  trackPseudoSelection = cms.PSet( 
    maxDistToAxis = cms.double( 0.07 ),
    totalHitsMin = cms.uint32( 0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dValMax = cms.double( 99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    qualityClass = cms.string( "any" ),
    jetDeltaRMax = cms.double( 0.3 ),
    normChi2Max = cms.double( 99999.9 ),
    pixelHitsMin = cms.uint32( 0 ),
    sip2dSigMin = cms.double( 2.0 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  trackSort = cms.string( "sip2dSig" ),
  SoftLeptonFlip = cms.bool( False ),
  trackFlip = cms.bool( False )
)
fragment.hltCombinedSecondaryVertexV2 = cms.ESProducer( "CombinedSecondaryVertexESProducer",
  recordLabel = cms.string( "HLT" ),
  categoryVariableName = cms.string( "vertexCategory" ),
  useTrackWeights = cms.bool( True ),
  useCategories = cms.bool( True ),
  pseudoMultiplicityMin = cms.uint32( 2 ),
  correctVertexMass = cms.bool( True ),
  trackSelection = cms.PSet( 
    max_pT_dRcut = cms.double( 0.1 ),
    b_dR = cms.double( 0.6263 ),
    min_pT = cms.double( 120.0 ),
    b_pT = cms.double( 0.3684 ),
    ptMin = cms.double( 0.0 ),
    max_pT_trackPTcut = cms.double( 3.0 ),
    max_pT = cms.double( 500.0 ),
    useVariableJTA = cms.bool( False ),
    maxDecayLen = cms.double( 5.0 ),
    qualityClass = cms.string( "any" ),
    normChi2Max = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 ),
    a_dR = cms.double( -0.001053 ),
    maxDistToAxis = cms.double( 0.07 ),
    totalHitsMin = cms.uint32( 0 ),
    a_pT = cms.double( 0.005263 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dValMax = cms.double( 99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    min_pT_dRcut = cms.double( 0.5 ),
    jetDeltaRMax = cms.double( 0.3 ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip2dSigMin = cms.double( -99999.9 )
  ),
  calibrationRecords = cms.vstring( 'CombinedSVIVFV2RecoVertex',
    'CombinedSVIVFV2PseudoVertex',
    'CombinedSVIVFV2NoVertex' ),
  trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
  charmCut = cms.double( 1.5 ),
  vertexFlip = cms.bool( False ),
  minimumTrackWeight = cms.double( 0.5 ),
  pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
  trackMultiplicityMin = cms.uint32( 3 ),
  trackPseudoSelection = cms.PSet( 
    max_pT_dRcut = cms.double( 0.1 ),
    b_dR = cms.double( 0.6263 ),
    min_pT = cms.double( 120.0 ),
    b_pT = cms.double( 0.3684 ),
    ptMin = cms.double( 0.0 ),
    max_pT_trackPTcut = cms.double( 3.0 ),
    max_pT = cms.double( 500.0 ),
    useVariableJTA = cms.bool( False ),
    maxDecayLen = cms.double( 5.0 ),
    qualityClass = cms.string( "any" ),
    normChi2Max = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 ),
    a_dR = cms.double( -0.001053 ),
    maxDistToAxis = cms.double( 0.07 ),
    totalHitsMin = cms.uint32( 0 ),
    a_pT = cms.double( 0.005263 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dValMax = cms.double( 99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    min_pT_dRcut = cms.double( 0.5 ),
    jetDeltaRMax = cms.double( 0.3 ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip2dSigMin = cms.double( 2.0 )
  ),
  trackSort = cms.string( "sip2dSig" ),
  SoftLeptonFlip = cms.bool( False ),
  trackFlip = cms.bool( False )
)
fragment.hltDisplacedDijethltESPPromptTrackCountingESProducer = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.1 ),
  useSignedImpactParameterSig = cms.bool( True ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
fragment.hltDisplacedDijethltESPTrackCounting2D1st = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( 0.05 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDistanceToJetAxis = cms.double( 9999999.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDecayLength = cms.double( 999999.0 ),
  nthTrack = cms.int32( 1 ),
  useSignedImpactParameterSig = cms.bool( False )
)
fragment.hltESPAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPAnalyticalPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" )
)
fragment.hltESPBwdAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPBwdAnalyticalPropagator" ),
  PropagationDirection = cms.string( "oppositeToMomentum" )
)
fragment.hltESPBwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPBwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.hltESPChi2ChargeLooseMeasurementEstimator16 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPChi2ChargeLooseMeasurementEstimator16" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 16.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPChi2ChargeMeasurementEstimator16 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 16.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPChi2ChargeMeasurementEstimator2000 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator2000" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 2000.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPChi2ChargeMeasurementEstimator30 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 30.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPChi2ChargeMeasurementEstimator9 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 9.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPChi2ChargeMeasurementEstimator9ForHI = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutForHI" ) ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator9ForHI" ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 9.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPChi2ChargeTightMeasurementEstimator16 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPChi2ChargeTightMeasurementEstimator16" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 16.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPChi2MeasurementEstimator100 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator100" ),
  nSigma = cms.double( 4.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 40.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1.0E12 )
)
fragment.hltESPChi2MeasurementEstimator16 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator16" ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 16.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPChi2MeasurementEstimator30 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator30" ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 30.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPChi2MeasurementEstimator9 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator9" ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 9.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPCloseComponentsMerger5D = cms.ESProducer( "CloseComponentsMergerESProducer5D",
  ComponentName = cms.string( "hltESPCloseComponentsMerger5D" ),
  MaxComponents = cms.int32( 12 ),
  DistanceMeasure = cms.string( "hltESPKullbackLeiblerDistance5D" )
)
fragment.hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPDetachedQuadStepChi2ChargeMeasurementEstimator9" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 9.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPDetachedQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPDetachedQuadStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.13 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
fragment.hltESPDetachedStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPDetachedStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.13 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
fragment.hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPDetachedTripletStepChi2ChargeMeasurementEstimator9" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 9.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPDetachedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPDetachedTripletStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.13 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
fragment.hltESPDisplacedDijethltPromptTrackCountingESProducer = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.1 ),
  useSignedImpactParameterSig = cms.bool( True ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
fragment.hltESPDisplacedDijethltPromptTrackCountingESProducerLong = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.2 ),
  useSignedImpactParameterSig = cms.bool( True ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
fragment.hltESPDisplacedDijethltTrackCounting2D1st = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( 0.05 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDistanceToJetAxis = cms.double( 9999999.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDecayLength = cms.double( 999999.0 ),
  nthTrack = cms.int32( 1 ),
  useSignedImpactParameterSig = cms.bool( False )
)
fragment.hltESPDisplacedDijethltTrackCounting2D2ndLong = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( 0.2 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDistanceToJetAxis = cms.double( 9999999.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDecayLength = cms.double( 999999.0 ),
  nthTrack = cms.int32( 2 ),
  useSignedImpactParameterSig = cms.bool( True )
)
fragment.hltESPDummyDetLayerGeometry = cms.ESProducer( "DetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPElectronMaterialEffects = cms.ESProducer( "GsfMaterialEffectsESProducer",
  BetheHeitlerParametrization = cms.string( "BetheHeitler_cdfmom_nC6_O5.par" ),
  EnergyLossUpdator = cms.string( "GsfBetheHeitlerUpdator" ),
  ComponentName = cms.string( "hltESPElectronMaterialEffects" ),
  MultipleScatteringUpdator = cms.string( "MultipleScatteringUpdator" ),
  Mass = cms.double( 5.11E-4 ),
  BetheHeitlerCorrection = cms.int32( 2 )
)
fragment.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorAny" )
)
fragment.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" )
)
fragment.hltESPFittingSmootherIT = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  ComponentName = cms.string( "hltESPFittingSmootherIT" ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPFittingSmootherRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  ComponentName = cms.string( "hltESPFittingSmootherRK" ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPFlexibleKFFittingSmoother = cms.ESProducer( "FlexibleKFFittingSmootherESProducer",
  ComponentName = cms.string( "hltESPFlexibleKFFittingSmoother" ),
  appendToDataLabel = cms.string( "" ),
  standardFitter = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
  looperFitter = cms.string( "hltESPKFFittingSmootherForLoopers" )
)
fragment.hltESPFwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPFwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
fragment.hltESPGlobalDetLayerGeometry = cms.ESProducer( "GlobalDetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPGlobalDetLayerGeometry" )
)
fragment.hltESPGsfElectronFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPGsfTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPGsfTrajectorySmoother" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  ComponentName = cms.string( "hltESPGsfElectronFittingSmoother" ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPGsfTrajectoryFitter = cms.ESProducer( "GsfTrajectoryFitterESProducer",
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectoryFitter" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  GeometricalPropagator = cms.string( "hltESPAnalyticalPropagator" )
)
fragment.hltESPGsfTrajectorySmoother = cms.ESProducer( "GsfTrajectorySmootherESProducer",
  ErrorRescaling = cms.double( 100.0 ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectorySmoother" ),
  GeometricalPropagator = cms.string( "hltESPBwdAnalyticalPropagator" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" )
)
fragment.hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPHighPtTripletStepChi2ChargeMeasurementEstimator30" ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 30.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPInitialStepChi2ChargeMeasurementEstimator30 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPInitialStepChi2ChargeMeasurementEstimator30" ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 30.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPInitialStepChi2MeasurementEstimator36 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPInitialStepChi2MeasurementEstimator36" ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 36.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPKFFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPKFTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmoother" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmoother" ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPKFFittingSmootherForL2Muon = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPKFFittingSmootherForLoopers = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForLoopers" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForLoopers" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  ComponentName = cms.string( "hltESPKFFittingSmootherForLoopers" ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPRKTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPRKTrajectorySmoother" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  ComponentName = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPKFTrajectoryFitterForLoopers = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForLoopers" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
fragment.hltESPKFTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmoother" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPKFTrajectorySmootherForLoopers = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForLoopers" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
fragment.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPKFUpdator = cms.ESProducer( "KFUpdatorESProducer",
  ComponentName = cms.string( "hltESPKFUpdator" )
)
fragment.hltESPKullbackLeiblerDistance5D = cms.ESProducer( "DistanceBetweenComponentsESProducer5D",
  ComponentName = cms.string( "hltESPKullbackLeiblerDistance5D" ),
  DistanceMeasure = cms.string( "KullbackLeibler" )
)
fragment.hltESPL3MuKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPLowPtQuadStepChi2ChargeMeasurementEstimator9" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 9.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPLowPtQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPLowPtQuadStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.16 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
fragment.hltESPLowPtStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPLowPtStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.16 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
fragment.hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPLowPtTripletStepChi2ChargeMeasurementEstimator9" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 9.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPLowPtTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPLowPtTripletStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.16 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
fragment.hltESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  UseStripStripQualityDB = cms.bool( True ),
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxBad = cms.uint32( 4 ),
      maxConsecutiveBad = cms.uint32( 2 )
    ),
    TIB = cms.PSet( 
      maxBad = cms.uint32( 4 ),
      maxConsecutiveBad = cms.uint32( 2 )
    ),
    TID = cms.PSet( 
      maxBad = cms.uint32( 4 ),
      maxConsecutiveBad = cms.uint32( 2 )
    ),
    TEC = cms.PSet( 
      maxBad = cms.uint32( 4 ),
      maxConsecutiveBad = cms.uint32( 2 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  SiStripQualityLabel = cms.string( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  MaskBadAPVFibers = cms.bool( True )
)
fragment.hltESPMixedStepClusterShapeHitFilter = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "hltESPMixedStepClusterShapeHitFilter" ),
  PixelShapeFileL1 = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par" )
)
fragment.hltESPMixedStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPMixedStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.11 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
fragment.hltESPMixedTripletStepChi2ChargeMeasurementEstimator16 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPMixedTripletStepChi2ChargeMeasurementEstimator16" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 16.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPMixedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPMixedTripletStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.11 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
fragment.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer( "MuonTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
)
fragment.hltESPPixelCPEGeneric = cms.ESProducer( "PixelCPEGenericESProducer",
  useLAAlignmentOffsets = cms.bool( False ),
  DoCosmics = cms.bool( False ),
  eff_charge_cut_highX = cms.double( 1.0 ),
  eff_charge_cut_highY = cms.double( 1.0 ),
  inflate_all_errors_no_trk_angle = cms.bool( False ),
  eff_charge_cut_lowY = cms.double( 0.0 ),
  eff_charge_cut_lowX = cms.double( 0.0 ),
  UseErrorsFromTemplates = cms.bool( True ),
  TruncatePixelCharge = cms.bool( True ),
  size_cutY = cms.double( 3.0 ),
  size_cutX = cms.double( 3.0 ),
  useLAWidthFromDB = cms.bool( False ),
  inflate_errors = cms.bool( False ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  PixelErrorParametrization = cms.string( "NOTcmsim" ),
  EdgeClusterErrorX = cms.double( 50.0 ),
  EdgeClusterErrorY = cms.double( 85.0 ),
  LoadTemplatesFromDB = cms.bool( True ),
  ComponentName = cms.string( "hltESPPixelCPEGeneric" ),
  MagneticFieldRecord = cms.ESInputTag( "" ),
  IrradiationBiasCorrection = cms.bool( False )
)
fragment.hltESPPixelCPETemplateReco = cms.ESProducer( "PixelCPETemplateRecoESProducer",
  DoLorentz = cms.bool( True ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  ComponentName = cms.string( "hltESPPixelCPETemplateReco" ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  speed = cms.int32( -2 ),
  UseClusterSplitter = cms.bool( False )
)
fragment.hltESPPixelLessStepChi2ChargeMeasurementEstimator16 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPPixelLessStepChi2ChargeMeasurementEstimator16" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 16.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPPixelLessStepClusterShapeHitFilter = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "hltESPPixelLessStepClusterShapeHitFilter" ),
  PixelShapeFileL1 = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par" )
)
fragment.hltESPPixelLessStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPPixelLessStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.11 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
fragment.hltESPPixelPairStepChi2ChargeMeasurementEstimator9 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPPixelPairStepChi2ChargeMeasurementEstimator9" ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 9.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1.0E12 )
)
fragment.hltESPPixelPairStepChi2MeasurementEstimator25 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPPixelPairStepChi2MeasurementEstimator25" ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 25.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPPixelPairTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPPixelPairTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.19 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
fragment.hltESPRKTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
fragment.hltESPRKTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKTrajectorySmoother" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
fragment.hltESPRungeKuttaTrackerPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( True )
)
fragment.hltESPSmartPropagator = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagator" )
)
fragment.hltESPSmartPropagatorAny = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAny" )
)
fragment.hltESPSmartPropagatorAnyOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAnyOpposite" )
)
fragment.hltESPSoftLeptonByDistance = cms.ESProducer( "LeptonTaggerByDistanceESProducer",
  distance = cms.double( 0.5 )
)
fragment.hltESPSteppingHelixPropagatorAlong = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "alongMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorAlong" )
)
fragment.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
)
fragment.hltESPStripCPEfromTrackAngle = cms.ESProducer( "StripCPEESProducer",
  ComponentType = cms.string( "StripCPEfromTrackAngle" ),
  ComponentName = cms.string( "hltESPStripCPEfromTrackAngle" ),
  parameters = cms.PSet( 
    mTIB_P1 = cms.double( 0.202 ),
    maxChgOneMIP = cms.double( 6000.0 ),
    mTEC_P0 = cms.double( -1.885 ),
    mTOB_P1 = cms.double( 0.253 ),
    mTEC_P1 = cms.double( 0.471 ),
    mLC_P2 = cms.double( 0.3 ),
    mLC_P1 = cms.double( 0.618 ),
    mTOB_P0 = cms.double( -1.026 ),
    mLC_P0 = cms.double( -0.326 ),
    useLegacyError = cms.bool( False ),
    mTIB_P0 = cms.double( -0.742 ),
    mTID_P1 = cms.double( 0.433 ),
    mTID_P0 = cms.double( -1.427 )
  )
)
fragment.hltESPTTRHBWithTrackAngle = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBWithTrackAngle" )
)
fragment.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPETemplateReco" ),
  ComponentName = cms.string( "hltESPTTRHBuilderAngleAndTemplate" )
)
fragment.hltESPTTRHBuilderPixelOnly = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderPixelOnly" )
)
fragment.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
)
fragment.hltESPTobTecStepChi2ChargeMeasurementEstimator16 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPTobTecStepChi2ChargeMeasurementEstimator16" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 16.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
fragment.hltESPTobTecStepClusterShapeHitFilter = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "hltESPTobTecStepClusterShapeHitFilter" ),
  PixelShapeFileL1 = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_loose.par" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase1_noL1.par" )
)
fragment.hltESPTobTecStepFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 30.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPTobTecStepRKFitter" ),
  MinNumberOfHits = cms.int32( 7 ),
  Smoother = cms.string( "hltESPTobTecStepRKSmoother" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  ComponentName = cms.string( "hltESPTobTecStepFitterSmoother" ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPTobTecStepFittingSmootherForLoopers = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 30.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPTobTecStepRKFitterForLoopers" ),
  MinNumberOfHits = cms.int32( 7 ),
  Smoother = cms.string( "hltESPTobTecStepRKSmootherForLoopers" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  ComponentName = cms.string( "hltESPTobTecStepFitterSmootherForLoopers" ),
  RejectTracks = cms.bool( True )
)
fragment.hltESPTobTecStepFlexibleKFFittingSmoother = cms.ESProducer( "FlexibleKFFittingSmootherESProducer",
  ComponentName = cms.string( "hltESPTobTecStepFlexibleKFFittingSmoother" ),
  appendToDataLabel = cms.string( "" ),
  standardFitter = cms.string( "hltESPTobTecStepFitterSmoother" ),
  looperFitter = cms.string( "hltESPTobTecStepFitterSmootherForLoopers" )
)
fragment.hltESPTobTecStepRKTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 7 ),
  ComponentName = cms.string( "hltESPTobTecStepRKFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPTobTecStepRKTrajectoryFitterForLoopers = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 7 ),
  ComponentName = cms.string( "hltESPTobTecStepRKFitterForLoopers" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPTobTecStepRKTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 7 ),
  ComponentName = cms.string( "hltESPTobTecStepRKSmoother" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPTobTecStepRKTrajectorySmootherForLoopers = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 7 ),
  ComponentName = cms.string( "hltESPTobTecStepRKSmootherForLoopers" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPTobTecStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTobTecStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.09 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
fragment.hltESPTrackAlgoPriorityOrder = cms.ESProducer( "TrackAlgoPriorityOrderESProducer",
  ComponentName = cms.string( "hltESPTrackAlgoPriorityOrder" ),
  appendToDataLabel = cms.string( "" ),
  algoOrder = cms.vstring(  )
)
fragment.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 100.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 0.0 ),
  allowSharedFirstHit = cms.bool( False )
)
fragment.hltESPTrajectoryFitterRK = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectoryFitterRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltESPTrajectorySmootherRK = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectorySmootherRK" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
fragment.hltPixelTracksCleanerBySharedHits = cms.ESProducer( "PixelTrackCleanerBySharedHitsESProducer",
  useQuadrupletAlgo = cms.bool( False ),
  ComponentName = cms.string( "hltPixelTracksCleanerBySharedHits" ),
  appendToDataLabel = cms.string( "" )
)
fragment.hltTrackCleaner = cms.ESProducer( "TrackCleanerESProducer",
  ComponentName = cms.string( "hltTrackCleaner" ),
  appendToDataLabel = cms.string( "" )
)
fragment.hoDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HODetIdAssociator" ),
  hcalRegion = cms.int32( 2 ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 30 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False ),
  includeME0 = cms.bool( False ),
  includeGEM = cms.bool( False )
)
fragment.muonDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "MuonDetIdAssociator" ),
  hcalRegion = cms.int32( 2 ),
  etaBinSize = cms.double( 0.125 ),
  nEta = cms.int32( 48 ),
  nPhi = cms.int32( 48 ),
  includeBadChambers = cms.bool( False ),
  includeME0 = cms.bool( False ),
  includeGEM = cms.bool( False )
)
fragment.muonSeededTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "muonSeededTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.1 ),
  ValidHitBonus = cms.double( 1000.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 1.0 ),
  allowSharedFirstHit = cms.bool( True )
)
fragment.navigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "SimpleNavigationSchool" ),
  SimpleMagneticField = cms.string( "ParabolicMf" )
)
fragment.preshowerDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "PreshowerDetIdAssociator" ),
  hcalRegion = cms.int32( 2 ),
  etaBinSize = cms.double( 0.1 ),
  nEta = cms.int32( 60 ),
  nPhi = cms.int32( 30 ),
  includeBadChambers = cms.bool( False ),
  includeME0 = cms.bool( False ),
  includeGEM = cms.bool( False )
)
fragment.siPixelQualityESProducer = cms.ESProducer( "SiPixelQualityESProducer",
  ListOfRecordToMerge = cms.VPSet( 
    cms.PSet(  record = cms.string( "SiPixelQualityFromDbRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiPixelDetVOffRcd" ),
      tag = cms.string( "" )
    )
  )
)
fragment.siPixelTemplateDBObjectESProducer = cms.ESProducer( "SiPixelTemplateDBObjectESProducer" )
fragment.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer( "SiStripBackPlaneCorrectionDepESProducer",
  LatencyRecord = cms.PSet( 
    label = cms.untracked.string( "" ),
    record = cms.string( "SiStripLatencyRcd" )
  ),
  BackPlaneCorrectionDeconvMode = cms.PSet( 
    label = cms.untracked.string( "deconvolution" ),
    record = cms.string( "SiStripBackPlaneCorrectionRcd" )
  ),
  BackPlaneCorrectionPeakMode = cms.PSet( 
    label = cms.untracked.string( "peak" ),
    record = cms.string( "SiStripBackPlaneCorrectionRcd" )
  )
)
fragment.siStripLorentzAngleDepESProducer = cms.ESProducer( "SiStripLorentzAngleDepESProducer",
  LatencyRecord = cms.PSet( 
    label = cms.untracked.string( "" ),
    record = cms.string( "SiStripLatencyRcd" )
  ),
  LorentzAngleDeconvMode = cms.PSet( 
    label = cms.untracked.string( "deconvolution" ),
    record = cms.string( "SiStripLorentzAngleRcd" )
  ),
  LorentzAnglePeakMode = cms.PSet( 
    label = cms.untracked.string( "peak" ),
    record = cms.string( "SiStripLorentzAngleRcd" )
  )
)

fragment.ThroughputService = cms.Service( "ThroughputService",
    dqmPath = cms.untracked.string( "HLT/Throughput" ),
    timeRange = cms.untracked.double( 60000.0 ),
    timeResolution = cms.untracked.double( 5.828 )
)

fragment.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet( 
    ),
    verbose = cms.untracked.bool( False )
)
fragment.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
fragment.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
fragment.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
fragment.hltL1EventNumberL1Fat = cms.EDFilter( "HLTL1NumberFilter",
    useTCDSEventNumber = cms.bool( True ),
    invert = cms.bool( False ),
    period = cms.uint32( 107 ),
    rawInput = cms.InputTag( "rawDataCollector" ),
    fedId = cms.int32( 1024 )
)
fragment.hltGtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::GTSetup" ),
    MinFeds = cms.uint32( 0 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    TMTCheck = cms.bool( True ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1404 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
fragment.hltGtStage2ObjectMap = cms.EDProducer( "L1TGlobalProducer",
    L1DataBxInEvent = cms.int32( 5 ),
    JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    AlgorithmTriggersUnmasked = cms.bool( True ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    PrintL1Menu = cms.untracked.bool( False ),
    PrescaleCSVFile = cms.string( "prescale_L1TGlobal.csv" ),
    Verbosity = cms.untracked.int32( 0 ),
    AlgoBlkInputTag = cms.InputTag( "hltGtStage2Digis" ),
    EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    ProduceL1GtDaqRecord = cms.bool( True ),
    PrescaleSet = cms.uint32( 1 ),
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    TriggerMenuLuminosity = cms.string( "startup" ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    GetPrescaleColumnFromData = cms.bool( False ),
    TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    BstLengthBytes = cms.int32( -1 ),
    MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' )
)
fragment.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
fragment.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
fragment.hltPrePhysics = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
fragment.hltRandomEventsFilter = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 3 )
)
fragment.hltPreRandom = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltL1sZeroBias = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_ZeroBias" ),
    L1EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
fragment.hltPreZeroBias = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023, 1024 )
)
fragment.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    moduleLabelPatternsToSkip = cms.vstring(  ),
    processName = cms.string( "@" ),
    moduleLabelPatternsToMatch = cms.vstring( 'hlt*' ),
    throw = cms.bool( False )
)
fragment.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
fragment.hltPreHLTAnalyzerEndpath = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltL1TGlobalSummary = cms.EDAnalyzer( "L1TGlobalSummary",
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    MaxBx = cms.int32( 0 ),
    DumpRecord = cms.bool( False ),
    psFileName = cms.string( "prescale_L1TGlobal.csv" ),
    ReadPrescalesFromFile = cms.bool( False ),
    AlgInputTag = cms.InputTag( "hltGtStage2Digis" ),
    MinBx = cms.int32( 0 ),
    psColumn = cms.int32( 0 ),
    DumpTrigResults = cms.bool( False ),
    DumpTrigSummary = cms.bool( True )
)
fragment.hltTrigReport = cms.EDAnalyzer( "HLTrigReport",
    ReferencePath = cms.untracked.string( "HLTriggerFinalPath" ),
    ReferenceRate = cms.untracked.double( 100.0 ),
    serviceBy = cms.untracked.string( "never" ),
    resetBy = cms.untracked.string( "never" ),
    reportBy = cms.untracked.string( "job" ),
    HLTriggerResults = cms.InputTag( 'TriggerResults','','@currentProcess' )
)

fragment.HLTL1UnpackerSequence = cms.Sequence( fragment.hltGtStage2Digis + fragment.hltGtStage2ObjectMap )
fragment.HLTBeamSpot = cms.Sequence( fragment.hltScalersRawToDigi + fragment.hltOnlineBeamSpot )
fragment.HLTBeginSequenceL1Fat = cms.Sequence( fragment.hltTriggerType + fragment.hltL1EventNumberL1Fat + fragment.HLTL1UnpackerSequence + fragment.HLTBeamSpot )
fragment.HLTEndSequence = cms.Sequence( fragment.hltBoolEnd )
fragment.HLTBeginSequenceRandom = cms.Sequence( fragment.hltRandomEventsFilter + fragment.hltGtStage2Digis )
fragment.HLTBeginSequence = cms.Sequence( fragment.hltTriggerType + fragment.HLTL1UnpackerSequence + fragment.HLTBeamSpot )

fragment.HLTriggerFirstPath = cms.Path( fragment.hltGetConditions + fragment.hltGetRaw + fragment.hltBoolFalse )
fragment.HLT_Physics_v7 = cms.Path( fragment.HLTBeginSequenceL1Fat + fragment.hltPrePhysics + fragment.HLTEndSequence )
fragment.HLT_Random_v3 = cms.Path( fragment.HLTBeginSequenceRandom + fragment.hltPreRandom + fragment.HLTEndSequence )
fragment.HLT_ZeroBias_v6 = cms.Path( fragment.HLTBeginSequence + fragment.hltL1sZeroBias + fragment.hltPreZeroBias + fragment.HLTEndSequence )
fragment.HLTriggerFinalPath = cms.Path( fragment.hltGtStage2Digis + fragment.hltScalersRawToDigi + fragment.hltFEDSelector + fragment.hltTriggerSummaryAOD + fragment.hltTriggerSummaryRAW + fragment.hltBoolFalse )
fragment.HLTAnalyzerEndpath = cms.EndPath( fragment.hltGtStage2Digis + fragment.hltPreHLTAnalyzerEndpath + fragment.hltL1TGlobalSummary + fragment.hltTrigReport )


fragment.HLTSchedule = cms.Schedule( *(fragment.HLTriggerFirstPath, fragment.HLT_Physics_v7, fragment.HLT_Random_v3, fragment.HLT_ZeroBias_v6, fragment.HLTriggerFinalPath, fragment.HLTAnalyzerEndpath ))


# dummyfy hltGetConditions in cff's
if 'hltGetConditions' in fragment.__dict__ and 'HLTriggerFirstPath' in fragment.__dict__ :
    fragment.hltDummyConditions = cms.EDFilter( "HLTBool",
        result = cms.bool( True )
    )
    fragment.HLTriggerFirstPath.replace(fragment.hltGetConditions,fragment.hltDummyConditions)

# add specific customizations
from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
fragment = customizeHLTforAll(fragment,"HIon")

from HLTrigger.Configuration.customizeHLTforCMSSW import customizeHLTforCMSSW
fragment = customizeHLTforCMSSW(fragment,"HIon")

# Eras-based customisations
from HLTrigger.Configuration.Eras import modifyHLTforEras
modifyHLTforEras(fragment)

