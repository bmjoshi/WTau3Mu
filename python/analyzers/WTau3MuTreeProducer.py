import ROOT
from CMGTools.WTau3Mu.analyzers.WTau3MuTreeProducerBase import WTau3MuTreeProducerBase
from PhysicsTools.HeppyCore.utils.deltar import deltaR

global muon_mass
muon_mass = 0.1056583745

class WTau3MuTreeProducer(WTau3MuTreeProducerBase):

    '''
    '''

    def declareVariables(self, setup):
        '''
        '''
        self.bookEvent(self.tree)
        self.bookTriplet(self.tree, 'cand')
        self.bookTriplet(self.tree, 'cand_refit')
        self.bookMuon(self.tree, 'mu1')
        self.bookMuon(self.tree, 'mu2')
        self.bookMuon(self.tree, 'mu3')
        self.bookMuon(self.tree, 'mu1_refit')
        self.bookMuon(self.tree, 'mu2_refit')
        self.bookMuon(self.tree, 'mu3_refit')        
        self.bookVertex(self.tree, 'tau_sv')

        # jet information
        self.bookJet(self.tree, 'jet1' , fill_extra=False)
        self.bookJet(self.tree, 'jet2' , fill_extra=False)
        self.bookJet(self.tree, 'bjet1', fill_extra=False)
        self.bookJet(self.tree, 'bjet2', fill_extra=False)
        self.var(self.tree, 'HTjets' )
        self.var(self.tree, 'HTbjets')
        self.var(self.tree, 'njets'  )
        self.var(self.tree, 'nbjets' )

        # generator information
        self.bookGenParticle(self.tree, 'gen_w')
        self.var            (self.tree, 'gen_w_pz')
        self.bookGenParticle(self.tree, 'mu1_refit_gen')
        self.bookGenParticle(self.tree, 'mu2_refit_gen')
        self.bookGenParticle(self.tree, 'mu3_refit_gen')
        self.bookGenParticle(self.tree, 'cand_refit_gen')
        self.bookParticle(self.tree, 'gen_met')
        self.var         (self.tree, 'gen_met_pz')
        self.bookParticle(self.tree, 'gen_nu')
        self.var         (self.tree, 'gen_nu_pz')

        # hadronic tau check
        if getattr(self.cfg_ana, 'tauh', False):
            self.bookParticle(self.tree, 'gen_tauh')
            self.var         (self.tree, 'gen_tauh_dm')

        # trigger information
        if hasattr(self.cfg_ana, 'fillL1') and self.cfg_ana.fillL1:
            self.bookL1object(self.tree, 'mu1_L1')
            self.bookL1object(self.tree, 'mu2_L1')
            self.bookL1object(self.tree, 'mu3_L1')
    
            self.var(self.tree, 'L1_mass12')
            self.var(self.tree, 'L1_mass13')
            self.var(self.tree, 'L1_mass23')
    
            self.var(self.tree, 'L1_dR12')
            self.var(self.tree, 'L1_dR13')
            self.var(self.tree, 'L1_dR23')
    
            self.var(self.tree, 'L1_pt12')
            self.var(self.tree, 'L1_pt13')
            self.var(self.tree, 'L1_pt23')

        self.var(self.tree, 'hlt_doublemu3_trk_tau3mu'                     )
        self.var(self.tree, 'hlt_isomu24'                                  )
        self.var(self.tree, 'hlt_isotkmu24'                                )
        self.var(self.tree, 'hlt_mu17_trkisovvl_mu8_trkisovvl_dz'          )
        self.var(self.tree, 'hlt_mu17_trkisovvl_tkmu8_trkisovvl_dz'        )
        self.var(self.tree, 'hlt_tkmu17_trkisovvl_tkmu8_trkisovvl_dz'      )
        self.var(self.tree, 'hlt_doublemu4_lowmassnonresonanttrk_displaced')
        self.var(self.tree, 'hlt_triplemu_12_10_5'                         )

        # BDT output
        self.var(self.tree, 'bdt_proba')
        self.var(self.tree, 'bdt_decision')

        # save HLT match type
        self.var(self.tree, 'mu1_hlt_doublemu3_trk_tau3mu_type')
        self.var(self.tree, 'mu2_hlt_doublemu3_trk_tau3mu_type')
        self.var(self.tree, 'mu3_hlt_doublemu3_trk_tau3mu_type')
        
        # more on weights
        self.var(self.tree, 'mu1_id_sf'   )
        self.var(self.tree, 'mu2_id_sf'   )
        self.var(self.tree, 'mu3_id_sf'   )

        self.var(self.tree, 'mu1_id_sf_e' )
        self.var(self.tree, 'mu2_id_sf_e' )
        self.var(self.tree, 'mu3_id_sf_e' )

        self.var(self.tree, 'mu1_hlt_sf'  )
        self.var(self.tree, 'mu2_hlt_sf'  )
        self.var(self.tree, 'mu3_hlt_sf'  )

        self.var(self.tree, 'mu1_hlt_sf_e')
        self.var(self.tree, 'mu2_hlt_sf_e')
        self.var(self.tree, 'mu3_hlt_sf_e')

        self.var(self.tree, 'trk_hlt_sf'  )
        self.var(self.tree, 'trk_hlt_sf_e')
        
    def process(self, event):
        '''
        '''
        self.readCollections(event.input)
        self.tree.reset()

        if not eval(self.skimFunction):
            return False

        self.fillEvent(self.tree, event)
        self.fillTriplet(self.tree, 'cand', event.tau3mu)
        
        self.fillTriplet(self.tree, 'cand', event.tau3mu)        
        self.fillMuon(self.tree, 'mu1', event.tau3mu.mu1())
        self.fillMuon(self.tree, 'mu2', event.tau3mu.mu2())
        self.fillMuon(self.tree, 'mu3', event.tau3mu.mu3())

        self.fillTriplet(self.tree, 'cand_refit', event.tau3muRefit)
        self.fillMuon(self.tree, 'mu1_refit', event.tau3muRefit.mu1())
        self.fillMuon(self.tree, 'mu2_refit', event.tau3muRefit.mu2())
        self.fillMuon(self.tree, 'mu3_refit', event.tau3muRefit.mu3())

        if hasattr(event.tau3muRefit, 'refittedVertex') and event.tau3muRefit.refittedVertex is not None:
            self.fillVertex(self.tree, 'tau_sv', event.tau3muRefit.refittedVertex)

        # generator information
        if hasattr(event, 'genw') and event.genw is not None: 
            self.fillGenParticle(self.tree, 'gen_w', event.genw)
            self.fill           (self.tree, 'gen_w_pz', event.genw.pz())

        if hasattr(event.tau3muRefit.mu1(), 'genp') and event.tau3muRefit.mu1().genp is not None: 
            self.fillGenParticle(self.tree, 'mu1_refit_gen', event.tau3muRefit.mu1().genp)
        if hasattr(event.tau3muRefit.mu2(), 'genp') and event.tau3muRefit.mu2().genp is not None: 
            self.fillGenParticle(self.tree, 'mu2_refit_gen', event.tau3muRefit.mu2().genp)
        if hasattr(event.tau3muRefit.mu3(), 'genp') and event.tau3muRefit.mu3().genp is not None: 
            self.fillGenParticle(self.tree, 'mu3_refit_gen', event.tau3muRefit.mu3().genp)

        if hasattr(event, 'genmet') and event.genmet is not None: 
            self.fillParticle(self.tree, 'gen_met'   , event.genmet     )
            self.fill        (self.tree, 'gen_met_pz', event.genmet.pz())

        if hasattr(event, 'gennufromw') and event.genmet is not None: 
            self.fillParticle(self.tree, 'gen_nu'   , event.gennufromw     )
            self.fill        (self.tree, 'gen_nu_pz', event.gennufromw.pz())

        if hasattr(event, 'gentau') and event.gentau is not None: 
            self.fillParticle(self.tree, 'cand_refit_gen', event.gentau)

        # trigger information
        if hasattr(self.cfg_ana, 'fillL1') and self.cfg_ana.fillL1:
            if hasattr(event.tau3muRefit.mu1(), 'L1'):
                self.fillL1object(self.tree, 'mu1_L1', event.tau3muRefit.mu1().L1)
            if hasattr(event.tau3muRefit.mu2(), 'L1'):
                self.fillL1object(self.tree, 'mu2_L1', event.tau3muRefit.mu2().L1)
            if hasattr(event.tau3muRefit.mu3(), 'L1'):
                self.fillL1object(self.tree, 'mu3_L1', event.tau3muRefit.mu3().L1)
    
            if hasattr(event.tau3muRefit.mu1(), 'L1') and hasattr(event.tau3muRefit.mu2(), 'L1'):

                l1mu1 = ROOT.TLorentzVector()
                l1mu1.SetPtEtaPhiM(
                    event.tau3muRefit.mu1().L1.pt(),
                    event.tau3muRefit.mu1().L1.eta(),
                    event.tau3muRefit.mu1().L1.phi(),
                    muon_mass,
                )
            
                l1mu2 = ROOT.TLorentzVector()
                l1mu2.SetPtEtaPhiM(
                    event.tau3muRefit.mu2().L1.pt(),
                    event.tau3muRefit.mu2().L1.eta(),
                    event.tau3muRefit.mu2().L1.phi(),
                    muon_mass,
                )
                        
                l1mass12 = (l1mu1 + l1mu2).M()
                l1dR12   = deltaR(l1mu1.Eta(), l1mu1.Phi(), l1mu2.Eta(), l1mu2.Phi())
                l1pt12   = (l1mu1 + l1mu2).Pt()
                
            self.fill(self.tree, 'L1_mass12', l1mass12)
            self.fill(self.tree, 'L1_dR12'  , l1dR12)
            self.fill(self.tree, 'L1_pt12'  , l1pt12)
    
            if hasattr(event.tau3muRefit.mu1(), 'L1') and hasattr(event.tau3muRefit.mu3(), 'L1'):

                l1mu1 = ROOT.TLorentzVector()
                l1mu1.SetPtEtaPhiM(
                    event.tau3muRefit.mu1().L1.pt(),
                    event.tau3muRefit.mu1().L1.eta(),
                    event.tau3muRefit.mu1().L1.phi(),
                    muon_mass,
                )
            
                l1mu3 = ROOT.TLorentzVector()
                l1mu3.SetPtEtaPhiM(
                    event.tau3muRefit.mu3().L1.pt(),
                    event.tau3muRefit.mu3().L1.eta(),
                    event.tau3muRefit.mu3().L1.phi(),
                    muon_mass,
                )
                        
                l1mass13 = (l1mu1 + l1mu3).M()
                l1dR13   = deltaR(l1mu1.Eta(), l1mu1.Phi(), l1mu3.Eta(), l1mu3.Phi())
                l1pt13   = (l1mu1 + l1mu3).Pt()
            
            self.fill(self.tree, 'L1_mass13', l1mass13)
            self.fill(self.tree, 'L1_dR13'  , l1dR13)
            self.fill(self.tree, 'L1_pt13'  , l1pt13)
    
            if hasattr(event.tau3muRefit.mu2(), 'L1') and hasattr(event.tau3muRefit.mu3(), 'L1'):

                l1mu2 = ROOT.TLorentzVector()
                l1mu2.SetPtEtaPhiM(
                    event.tau3muRefit.mu2().L1.pt(),
                    event.tau3muRefit.mu2().L1.eta(),
                    event.tau3muRefit.mu2().L1.phi(),
                    muon_mass,
                )
            
                l1mu3 = ROOT.TLorentzVector()
                l1mu3.SetPtEtaPhiM(
                    event.tau3muRefit.mu3().L1.pt(),
                    event.tau3muRefit.mu3().L1.eta(),
                    event.tau3muRefit.mu3().L1.phi(),
                    muon_mass,
                )
                        
                l1mass23 = (l1mu2 + l1mu3).M()
                l1dR23   = deltaR(l1mu2.Eta(), l1mu2.Phi(), l1mu3.Eta(), l1mu3.Phi())
                l1pt23   = (l1mu2 + l1mu3).Pt()
            
            self.fill(self.tree, 'L1_mass23', l1mass23)
            self.fill(self.tree, 'L1_dR23'  , l1dR23)
            self.fill(self.tree, 'L1_pt23'  , l1pt23)

        # HLT bits & matches
        self.fill(self.tree, 'hlt_doublemu3_trk_tau3mu'                     , any('HLT_DoubleMu3_Trk_Tau3mu'                      in name for name in event.tau3mu.hltmatched))
        self.fill(self.tree, 'hlt_isomu24'                                  , any('HLT_IsoMu24'                                   in name for name in event.tau3mu.hltmatched))
        self.fill(self.tree, 'hlt_isotkmu24'                                , any('HLT_IsoTkMu24'                                 in name for name in event.tau3mu.hltmatched))
        self.fill(self.tree, 'hlt_mu17_trkisovvl_mu8_trkisovvl_dz'          , any('HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'           in name for name in event.tau3mu.hltmatched))
        self.fill(self.tree, 'hlt_mu17_trkisovvl_tkmu8_trkisovvl_dz'        , any('HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'         in name for name in event.tau3mu.hltmatched))
        self.fill(self.tree, 'hlt_tkmu17_trkisovvl_tkmu8_trkisovvl_dz'      , any('HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ'       in name for name in event.tau3mu.hltmatched))
        self.fill(self.tree, 'hlt_doublemu4_lowmassnonresonanttrk_displaced', any('HLT_DoubleMu4_LowMassNonResonantTrk_Displaced' in name for name in event.tau3mu.hltmatched))
        self.fill(self.tree, 'hlt_triplemu_12_10_5'                         , any('HLT_TripleMu_12_10_5'                          in name for name in event.tau3mu.hltmatched))
    
        # BDT output
        if hasattr(event, 'bdt_proba'):
            self.fill(self.tree, 'bdt_proba', event.bdt_proba)
        if hasattr(event, 'bdt_decision'):
            self.fill(self.tree, 'bdt_decision', event.bdt_decision)
 
        # jet variables
        if len(event.cleanJets)>0:
            self.fillJet(self.tree, 'jet1', event.cleanJets[0], fill_extra=False)
        if len(event.cleanJets)>1:
            self.fillJet(self.tree, 'jet2', event.cleanJets[1], fill_extra=False)
        if len(event.cleanBJets)>0:
            self.fillJet(self.tree, 'bjet1', event.cleanBJets[0], fill_extra=False)
        if len(event.cleanBJets)>1:
            self.fillJet(self.tree, 'bjet2', event.cleanBJets[1], fill_extra=False)

        self.fill(self.tree, 'HTjets' , event.HT_cleanJets   )
        self.fill(self.tree, 'HTbjets', event.HT_bJets       )
        self.fill(self.tree, 'njets'  , len(event.cleanJets) )
        self.fill(self.tree, 'nbjets' , len(event.cleanBJets))

        # save HLT match type
        try:
            self.fill(self.tree, 'mu1_hlt_doublemu3_trk_tau3mu_type', event.tau3mu.best_trig_match[1]['HLT_DoubleMu3_Trk_Tau3mu'].triggerObjectTypes()[0])
            self.fill(self.tree, 'mu2_hlt_doublemu3_trk_tau3mu_type', event.tau3mu.best_trig_match[2]['HLT_DoubleMu3_Trk_Tau3mu'].triggerObjectTypes()[0])
            self.fill(self.tree, 'mu3_hlt_doublemu3_trk_tau3mu_type', event.tau3mu.best_trig_match[3]['HLT_DoubleMu3_Trk_Tau3mu'].triggerObjectTypes()[0])
        except:
            pass

        # weights
        self.fill(self.tree, 'mu1_id_sf'   , getattr(event.tau3mu.mu1(), 'idweight'      , 1.))
        self.fill(self.tree, 'mu2_id_sf'   , getattr(event.tau3mu.mu2(), 'idweight'      , 1.))
        self.fill(self.tree, 'mu3_id_sf'   , getattr(event.tau3mu.mu3(), 'idweight'      , 1.))

        self.fill(self.tree, 'mu1_id_sf_e' , getattr(event.tau3mu.mu1(), 'idweightunc'   , 0.))
        self.fill(self.tree, 'mu2_id_sf_e' , getattr(event.tau3mu.mu2(), 'idweightunc'   , 0.))
        self.fill(self.tree, 'mu3_id_sf_e' , getattr(event.tau3mu.mu3(), 'idweightunc'   , 0.))

        self.fill(self.tree, 'mu1_hlt_sf'  , getattr(event.tau3mu.mu1(), 'HLTWeightMU'   , 1.))
        self.fill(self.tree, 'mu2_hlt_sf'  , getattr(event.tau3mu.mu2(), 'HLTWeightMU'   , 1.))
        self.fill(self.tree, 'mu3_hlt_sf'  , getattr(event.tau3mu.mu3(), 'HLTWeightMU'   , 1.))

        self.fill(self.tree, 'mu1_hlt_sf_e', getattr(event.tau3mu.mu1(), 'HLTWeightUncMU', 0.))
        self.fill(self.tree, 'mu2_hlt_sf_e', getattr(event.tau3mu.mu2(), 'HLTWeightUncMU', 0.))
        self.fill(self.tree, 'mu3_hlt_sf_e', getattr(event.tau3mu.mu3(), 'HLTWeightUncMU', 0.))

        self.fill(self.tree, 'trk_hlt_sf'  , getattr(event.tau3mu      , 'HLTWeightTK'   , 1.))
        self.fill(self.tree, 'trk_hlt_sf_e', getattr(event.tau3mu      , 'HLTWeightUncTK', 0.))

#         import pdb ; pdb.set_trace() 

        # hadronic tau check
        if getattr(self.cfg_ana, 'tauh', False):
            for itau in event.gentaus:
                if deltaR(itau, event.tau3muRefit.p4Muons())<0.1:
                    self.fillParticle(self.tree, 'gen_tauh', itau)
                    itau = event.gentaus[0]
                    dm = -99
                    ncharged = 0
                    nneutral = 0
                    nele     = 0
                    nmu      = 0
                    ntau     = 0
                    for idau in range(itau.numberOfDaughters()):
                        print itau.daughter(idau).pdgId()
                        if abs(itau.daughter(idau).pdgId()) in [11]      : nele     +=1
                        if abs(itau.daughter(idau).pdgId()) in [13]      : nmu      +=1
                        if abs(itau.daughter(idau).pdgId()) in [15]      : ntau     +=1
                        if abs(itau.daughter(idau).pdgId()) in [321, 211]: ncharged +=1
                        if abs(itau.daughter(idau).pdgId()) in [111]     : nneutral +=1
                    if ncharged>0:
                        dm = (ncharged-1)*5 + nneutral
                    if nmu>0:
                        dm = -13
                    if nele>0:
                        dm = -11
                    if ntau>0:
                        dm = -15
                    self.fill(self.tree, 'gen_tauh_dm', dm)
                    break

        self.fillTree(event)

