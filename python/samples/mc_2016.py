import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
creator = ComponentCreator()

# first private production
WToTauTo3Mu = cfg.MCComponent(
    dataset       = 'WToTauTo3Mu',
    name          = 'WToTauTo3Mu',
    files         = [
        '/eos/user/m/manzoni/WTau3Mu/signal/tau3mu_mvamet.root',
#         '/afs/cern.ch/work/m/mverzett/public/perRic/t3mMINIAODSIM/t3mu_MINIAODSIM_0.root',
#         '/afs/cern.ch/work/m/mverzett/public/perRic/t3mMINIAODSIM/t3mu_MINIAODSIM_1.root',
#         '/afs/cern.ch/work/m/mverzett/public/perRic/t3mMINIAODSIM/t3mu_MINIAODSIM_2.root',
#         '/afs/cern.ch/work/m/mverzett/public/perRic/t3mMINIAODSIM/t3mu_MINIAODSIM_3.root',
#         '/afs/cern.ch/work/m/mverzett/public/perRic/t3mMINIAODSIM/t3mu_MINIAODSIM_4.root',
#         '/afs/cern.ch/work/m/mverzett/public/perRic/t3mMINIAODSIM/t3mu_MINIAODSIM_5.root',
#         '/afs/cern.ch/work/m/mverzett/public/perRic/t3mMINIAODSIM/t3mu_MINIAODSIM_6.root',
#         '/afs/cern.ch/work/m/mverzett/public/perRic/t3mMINIAODSIM/t3mu_MINIAODSIM_7.root',
#         '/afs/cern.ch/work/m/mverzett/public/perRic/t3mMINIAODSIM/t3mu_MINIAODSIM_8.root',
#         '/afs/cern.ch/work/m/mverzett/public/perRic/t3mMINIAODSIM/t3mu_MINIAODSIM_9.root',
          #### with MVA MET computed
#           '/afs/cern.ch/work/m/manzoni/diTau2015/CMSSW_9_2_2_minimal_recipe/src/RecoMET/METPUSubtraction/test/output.root',
    ],
    xSection      = 21490.9, # this uses the correct tau BR from the PDG # 20508.9 * 1.e-7, # W to lep nu / 3.[pb] x BR
#     xSection      = 20508.9 * 0.005, # W to lep nu / 3.[pb] x BR
    nGenEvents    = 20000.,
    triggers      = ['HLT_DoubleMu3_Trk_Tau3mu_v%d' %i for i in range(1, 5)],
    effCorrFactor = 1,
)


WToTauTo3Mu_M1p55 = cfg.MCComponent(dataset = 'WToTauTo3Mu_M1p55', name = 'WToTauTo3Mu_M1p55', files = ['/eos/user/m/manzoni/WTau3Mu/signalFakeTauMass/tau3mu_m1p55_mvamet.root'], xSection = 1, nGenEvents = 5000., triggers = ['HLT_DoubleMu3_Trk_Tau3mu_v%d' %i for i in range(1, 5)], effCorrFactor = 1)
WToTauTo3Mu_M1p60 = cfg.MCComponent(dataset = 'WToTauTo3Mu_M1p60', name = 'WToTauTo3Mu_M1p60', files = ['/eos/user/m/manzoni/WTau3Mu/signalFakeTauMass/tau3mu_m1p60_mvamet.root'], xSection = 1, nGenEvents = 5000., triggers = ['HLT_DoubleMu3_Trk_Tau3mu_v%d' %i for i in range(1, 5)], effCorrFactor = 1)
WToTauTo3Mu_M1p65 = cfg.MCComponent(dataset = 'WToTauTo3Mu_M1p65', name = 'WToTauTo3Mu_M1p65', files = ['/eos/user/m/manzoni/WTau3Mu/signalFakeTauMass/tau3mu_m1p65_mvamet.root'], xSection = 1, nGenEvents = 5000., triggers = ['HLT_DoubleMu3_Trk_Tau3mu_v%d' %i for i in range(1, 5)], effCorrFactor = 1)
WToTauTo3Mu_M1p70 = cfg.MCComponent(dataset = 'WToTauTo3Mu_M1p70', name = 'WToTauTo3Mu_M1p70', files = ['/eos/user/m/manzoni/WTau3Mu/signalFakeTauMass/tau3mu_m1p70_mvamet.root'], xSection = 1, nGenEvents = 5000., triggers = ['HLT_DoubleMu3_Trk_Tau3mu_v%d' %i for i in range(1, 5)], effCorrFactor = 1)
WToTauTo3Mu_M1p85 = cfg.MCComponent(dataset = 'WToTauTo3Mu_M1p85', name = 'WToTauTo3Mu_M1p85', files = ['/eos/user/m/manzoni/WTau3Mu/signalFakeTauMass/tau3mu_m1p85_mvamet.root'], xSection = 1, nGenEvents = 5000., triggers = ['HLT_DoubleMu3_Trk_Tau3mu_v%d' %i for i in range(1, 5)], effCorrFactor = 1)
WToTauTo3Mu_M1p90 = cfg.MCComponent(dataset = 'WToTauTo3Mu_M1p90', name = 'WToTauTo3Mu_M1p90', files = ['/eos/user/m/manzoni/WTau3Mu/signalFakeTauMass/tau3mu_m1p90_mvamet.root'], xSection = 1, nGenEvents = 5000., triggers = ['HLT_DoubleMu3_Trk_Tau3mu_v%d' %i for i in range(1, 5)], effCorrFactor = 1)
WToTauTo3Mu_M1p95 = cfg.MCComponent(dataset = 'WToTauTo3Mu_M1p95', name = 'WToTauTo3Mu_M1p95', files = ['/eos/user/m/manzoni/WTau3Mu/signalFakeTauMass/tau3mu_m1p95_mvamet.root'], xSection = 1, nGenEvents = 5000., triggers = ['HLT_DoubleMu3_Trk_Tau3mu_v%d' %i for i in range(1, 5)], effCorrFactor = 1)

all_wtau3mu = [
    WToTauTo3Mu,
    WToTauTo3Mu_M1p55,
    WToTauTo3Mu_M1p60,
    WToTauTo3Mu_M1p65,
    WToTauTo3Mu_M1p70,
    WToTauTo3Mu_M1p85,
    WToTauTo3Mu_M1p90,
    WToTauTo3Mu_M1p95,
]


WJetsToLNu_amc     = creator.makeMCComponent(name = 'WJetsToLNu_amc'    , dataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'     , user = 'CMS', pattern = '.*root', xSec = (8580+11370)*0.1063*3 , useAAA  = True)
WJetsToLNu_amc_ext = creator.makeMCComponent(name = 'WJetsToLNu_amc_ext', dataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/MINIAODSIM', user = 'CMS', pattern = '.*root', xSec = (8580+11370)*0.1063*3 , useAAA  = True)
WJetsToLNu_mg      = creator.makeMCComponent(name = 'WJetsToLNu_mg'     , dataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'      , user = 'CMS', pattern = '.*root', xSec = (8580+11370)*0.1063*3 , useAAA  = True)
WJetsToLNu_mg_ext  = creator.makeMCComponent(name = 'WJetsToLNu_mg_ext' , dataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM' , user = 'CMS', pattern = '.*root', xSec = (8580+11370)*0.1063*3 , useAAA  = True)

all_wjets = [
    WJetsToLNu_amc    ,
    WJetsToLNu_amc_ext,
    WJetsToLNu_mg     ,
    WJetsToLNu_mg_ext ,
]


DYJetsToLL_M50_ext1 = creator.makeMCComponent(name = 'DYJetsToLL_M50_ext1' , dataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM' , user = 'CMS', pattern = '.*root', xSec = (8580+11370)*0.1063*3 , useAAA  = True)
DYJetsToLL_M50_ext2 = creator.makeMCComponent(name = 'DYJetsToLL_M50_ext2' , dataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM' , user = 'CMS', pattern = '.*root', xSec = (8580+11370)*0.1063*3 , useAAA  = True)

all_dyjets = [
    DYJetsToLL_M50_ext1,
    DYJetsToLL_M50_ext2,
]




