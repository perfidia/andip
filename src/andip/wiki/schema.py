#-*- coding: utf-8 -*-

class Schema(object):
        
    def get_word_present(self,conj_type, forma, liczba, osoba, base_word):
        new_end = self.conjugation[conj_type]['forma'][forma][liczba][osoba]
        return base_word.replace(str(self.conjugation[conj_type]['koncowka']), str(new_end))
    
    def get_word_past(self,conj_type, forma, liczba, rodzaj, osoba, base_word):
        new_end = self.conjugation[conj_type]['forma'][forma][liczba][rodzaj][osoba]
        return  base_word.replace(self.conjugation[conj_type]['koncowka'], new_end)
        
        
    conjugation = {
                   'I' : {
                          'koncowka' : 'ać',
                          'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'am',
                                                                           'druga': 'asz',
                                                                           'trzecia': 'a'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'amy',
                                                                            'druga' : 'acie',
                                                                            'trzecia' : 'ają'
                                                                    }
                                                           }
                                    },
                                    'czas przeszły' : {
                                                       'pojedyńcza' : {
                                                                       'm' : {
                                                                                        'pierwsza' : 'ałem',
                                                                                        'druga' : 'ałeś',
                                                                                        'trzecia' : 'ał'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'ałam',
                                                                                        'druga' : 'ałaś',
                                                                                        'trzecia' : 'ała'
                                                                                   },
                                                                       'n' : {
                                                                                        'pierwsza' : 'ałom',
                                                                                        'druga' : 'ałoś',
                                                                                        'trzecia' : 'ało'
                                                                                   }
                                                                      },
                                                       'mnoga' : {
                                                                        'm' : {
                                                                                        'pierwsza' : 'aliśmy',
                                                                                        'druga' : 'aliście',
                                                                                        'trzecia' : 'ali'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'ałyśmy',
                                                                                        'druga' : 'ałyście',
                                                                                        'trzecia' : 'ały'
                                                                                   },
                                                                       'n' : {
                                                                                        'pierwsza' : 'ałyśmy',
                                                                                        'druga' : 'ałyście',
                                                                                        'trzecia' : 'ały'
                                                                                   }
                                                                  }
                                            }
                    },
                   'II' : {
                           'koncowka' : 'eć',
                           'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'em',
                                                                           'druga': 'esz',
                                                                           'trzecia': 'e'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'emy',
                                                                            'druga' : 'ecie',
                                                                            'trzecia' : 'eją'
                                                                    }
                                                           }
                                    },
                                    'czas przeszły' : {
                                                       'pojedyńcza' : {
                                                                       'm' : {
                                                                                        'pierwsza' : 'ałem',
                                                                                        'druga' : 'ałeś',
                                                                                        'trzecia' : 'ał'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'ałam',
                                                                                        'druga' : 'ałaś',
                                                                                        'trzecia' : 'ała'
                                                                                   },
                                                                       'n' : {
                                                                                        'pierwsza' : 'ałom',
                                                                                        'druga' : 'ałoś',
                                                                                        'trzecia' : 'ało'
                                                                                   }
                                                                      },
                                                       'mnoga' : {
                                                                        'm' : {
                                                                                        'pierwsza' : 'eliśmy',
                                                                                        'druga' : 'eliście',
                                                                                        'trzecia' : 'eli'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'ałyśmy',
                                                                                        'druga' : 'ałyście',
                                                                                        'trzecia' : 'ały'
                                                                                   },
                                                                       'n' : {
                                                                                        'pierwsza' : 'ałyśmy',
                                                                                        'druga' : 'ałyście',
                                                                                        'trzecia' : 'ały'
                                                                                   }
                                                                  }
                                            }
                    },
                   'III' : {
                            'koncowka' : 'eć',
                            'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'eję',
                                                                           'druga': 'ejesz',
                                                                           'trzecia': 'eje'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'ejemy',
                                                                            'druga' : 'ejecie',
                                                                            'trzecia' : 'eją'
                                                                    }
                                                           }
                                    },
                                    'czas przeszły' : {
                                                       'pojedyńcza' : {
                                                                       'm' : {
                                                                                        'pierwsza' : 'ałem',
                                                                                        'druga' : 'ałeś',
                                                                                        'trzecia' : 'ał'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'ałam',
                                                                                        'druga' : 'ałaś',
                                                                                        'trzecia' : 'ała'
                                                                                   },
                                                                       'n' : {
                                                                                        'pierwsza' : 'ałom',
                                                                                        'druga' : 'ałoś',
                                                                                        'trzecia' : 'ało'
                                                                                   }
                                                                      },
                                                       'mnoga' : {
                                                                        'm' : {
                                                                                        'pierwsza' : 'liśmy',
                                                                                        'druga' : 'eliście',
                                                                                        'trzecia' : 'eli'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'ałyśmy',
                                                                                        'druga' : 'ałyście',
                                                                                        'trzecia' : 'ały'
                                                                                   },
                                                                       'n' : {
                                                                                        'pierwsza' : 'ałyśmy',
                                                                                        'druga' : 'ałyście',
                                                                                        'trzecia' : 'ały'
                                                                                   }
                                                                  }
                                            }
                    },
                   'IV' : {
                           'koncowka' : 'ować',
                           'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'uję',
                                                                           'druga': 'ujesz',
                                                                           'trzecia': 'uje'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'ujemy',
                                                                            'druga' : 'ujecie',
                                                                            'trzecia' : 'ują'
                                                                    }
                                                           }
                                    ,
                                    'czas przeszły' : {
                                                       'pojedyńcza' : {
                                                                       'm' : {
                                                                                        'pierwsza' : 'owałem',
                                                                                        'druga' : 'owałeś',
                                                                                        'trzecia' : 'ował'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'owałam',
                                                                                        'druga' : 'owałaś',
                                                                                        'trzecia' : 'owała'
                                                                                   },
                                                                       'n' : {
                                                                                        'pierwsza' : 'owałom',
                                                                                        'druga' : 'owałoś',
                                                                                        'trzecia' : 'owało'
                                                                                   }
                                                                      },
                                                       'mnoga' : {
                                                                        'm' : {
                                                                                        'pierwsza' : 'owaliśmy',
                                                                                        'druga' : 'owaliście',
                                                                                        'trzecia' : 'owali'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'owałyśmy',
                                                                                        'druga' : 'owałyście',
                                                                                        'trzecia' : 'owały'
                                                                                   },
                                                                       'n' : {
                                                                                        'pierwsza' : 'owałyśmy',
                                                                                        'druga' : 'owałyście',
                                                                                        'trzecia' : 'owały'
                                                                                   }
                                                                  }
                                            }
                                     }
                    },
                    'Va' : {
                            'koncowka' : 'nąć',
                            'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'nę',
                                                                           'druga': 'niesz',
                                                                           'trzecia': 'nie'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'niemy',
                                                                            'druga' : 'niecie',
                                                                            'trzecia' : 'ną'
                                                                    }
                                                           }
                                    },
                                    'czas przeszły' : {
                                                       'pojedyńcza' : {
                                                                       'm' : {
                                                                                        'pierwsza' : 'nąłem',
                                                                                        'druga' : 'nąłeś',
                                                                                        'trzecia' : 'nął'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'nęłam',
                                                                                        'druga' : 'nęłaś',
                                                                                        'trzecia' : 'nęła'
                                                                                   },
                                                                       'n' : {
                                                                                        'trzecia' : 'nęło'
                                                                                   }
                                                                      },
                                                       'mnoga' : {
                                                                        'm' : {
                                                                                        'pierwsza' : 'nęliśmy',
                                                                                        'druga' : 'nęliście',
                                                                                        'trzecia' : 'nęli'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'nęłyśmy',
                                                                                        'druga' : 'nęłyście',
                                                                                        'trzecia' : 'nęły'
                                                                                   },
                                                                       'n' : {
                                                                                        'pierwsza' : 'nęłyśmy',
                                                                                        'druga' : 'nęłyście',
                                                                                        'trzecia' : 'nęły'
                                                                                   }
                                                                  }
                                            }
                    },
                    'Vb' : {
                            'koncowka' : 'nąć',
                            'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'nę',
                                                                           'druga': 'niesz',
                                                                           'trzecia': 'nie'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'niemy',
                                                                            'druga' : 'niecie',
                                                                            'trzecia' : 'ną'
                                                                    }
                                                           }
                                    },
                                    'czas przeszły' : {
                                                       'pojedyńcza' : {
                                                                       'm' : {
                                                                                        'pierwsza' : 'nąłem',
                                                                                        'druga' : 'nąłeś',
                                                                                        'trzecia' : 'nął'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'nęłam',
                                                                                        'druga' : 'nęłaś',
                                                                                        'trzecia' : 'nęła'
                                                                                   },
                                                                       'n' : {
                                                                                        'trzecia' : 'nęło'
                                                                                   }
                                                                      },
                                                       'mnoga' : {
                                                                        'm' : {
                                                                                        'pierwsza' : 'nęliśmy',
                                                                                        'druga' : 'nęliście',
                                                                                        'trzecia' : 'nęli'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'nęłyśmy',
                                                                                        'druga' : 'nęłyście',
                                                                                        'trzecia' : 'nęły'
                                                                                   },
                                                                       'n' : {
                                                                                        'pierwsza' : 'nęłyśmy',
                                                                                        'druga' : 'nęłyście',
                                                                                        'trzecia' : 'nęły'
                                                                                   }
                                                                  }
                                            }
                    },
                    'Vc' : {
                            'koncowka' : 'nąć',
                            'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'nę',
                                                                           'druga': 'niesz',
                                                                           'trzecia': 'nie'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'niemy',
                                                                            'druga' : 'niecie',
                                                                            'trzecia' : 'ną'
                                                                    }
                                                           }
                                    }
                    },
                   'VIa' : {
                           'koncowka' : 'ić',
                           'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'ię',
                                                                           'druga': 'isz',
                                                                           'trzecia': 'i'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'imy',
                                                                            'druga' : 'icie',
                                                                            'trzecia' : 'ią'
                                                                    }
                                    },
                                    'czas przeszły' : {
                                                       'pojedyńcza' : {
                                                                       'm' : {
                                                                                        'pierwsza' : 'iłem',
                                                                                        'druga' : 'iłeś',
                                                                                        'trzecia' : 'ił'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'iła',
                                                                                        'druga' : 'iłaś',
                                                                                        'trzecia' : 'iła'
                                                                                   },
                                                                       'n' : {
                                                                                        'trzecia' : 'iło'
                                                                                   }
                                                                      },
                                                       'mnoga' : {
                                                                        'm' : {
                                                                                        'pierwsza' : 'iliśmy',
                                                                                        'druga' : 'iliście',
                                                                                        'trzecia' : 'ili'
                                                                                  },
                                                                       'ż' : {
                                                                                        'pierwsza' : 'iłyśmy',
                                                                                        'druga' : 'iłyście',
                                                                                        'trzecia' : 'iły'
                                                                                   },
                                                                       'n' : {
                                                                                        'trzecia' : 'nęło'

                                                                      },
                                                                  }
                                            }
                                    }
                    },
                   'VIb' : {
                           'koncowka' : 'yć',
                           'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'ę',
                                                                           'druga': 'ysz',
                                                                           'trzecia': 'y'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'ymy',
                                                                            'druga' : 'ycie',
                                                                            'trzecia' : 'ą'
                                                                    }
                                                           }
                                    },
                                    'czas przeszly' : {
                                                       'pojedyncza' : {
                                                                       'meski' : {
                                                                                        'pierwsza' : 'ałem',
                                                                                        'druga' : 'ałeś',
                                                                                        'trzecia' : 'ał'
                                                                                  },
                                                                       'zenski' : {
                                                                                        'pierwsza' : 'ała',
                                                                                        'druga' : 'ałaś',
                                                                                        'trzecia' : 'ała'
                                                                                   },
                                                                       'nijaki' : {
                                                                                        'trzecia' : 'ało'
                                                                                   }
                                                                      },
                                                       'mnoga' : {
                                                                        'meski' : {
                                                                                        'pierwsza' : 'eliśmy',
                                                                                        'druga' : 'eliście',
                                                                                        'trzecia' : 'eli'
                                                                                  },
                                                                       'zenski' : {
                                                                                        'pierwsza' : 'ałyśmy',
                                                                                        'druga' : 'ałyście',
                                                                                        'trzecia' : 'ały'
                                                                                   },
                                                                       'nijaki' : {
                                                                                        'pierwsza' : 'ałyśmy',
                                                                                        'druga' : 'ałyście',
                                                                                        'trzecia' : 'ały'

                                                                      },
                                                                  }
                                            }
                    },
                   'VIIa' : {
                           'koncowka' : 'eć',
                           'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'ę',
                                                                           'druga': 'isz',
                                                                           'trzecia': 'i'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'imy',
                                                                            'druga' : 'icie',
                                                                            'trzecia' : 'ą'
                                                                    }
                                                           }
                                    }
                    },
                   'VIIb' : {
                           'koncowka' : 'eć',
                           'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'ę',
                                                                           'druga': 'ysz',
                                                                           'trzecia': 'y'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'ymy',
                                                                            'druga' : 'ycie',
                                                                            'trzecia' : 'ą'
                                                                    }
                                                           }
                                    }
                    },
                   'VIIIa' : {
                           'koncowka' : 'ywać',
                           'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'uję',
                                                                           'druga': 'ujesz',
                                                                           'trzecia': 'uje'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'ujemy',
                                                                            'druga' : 'ujecie',
                                                                            'trzecia' : 'ują'
                                                                    }
                                                           }
                                    }
                    },
                   'VIIIb' : {
                           'koncowka' : 'iwać',
                           'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'uję',
                                                                           'druga': 'ujesz',
                                                                           'trzecia': 'uje'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'ujemy',
                                                                            'druga' : 'ujecie',
                                                                            'trzecia' : 'ują'
                                                                    }
                                                           }
                                    }
                    },
                   'IX' : {
                           'koncowka' : 'ać',
                           'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'ę',
                                                                           'druga': 'esz',
                                                                           'trzecia': 'e'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'emy',
                                                                            'druga' : 'ecie',
                                                                            'trzecia' : 'ą'
                                                                    }
                                                           }
                                    }
                    },
                   'Xa' : {
                           'koncowka' : 'ć',
                           'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'ję',
                                                                           'druga': 'jesz',
                                                                           'trzecia': 'je'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'jemy',
                                                                            'druga' : 'jecie',
                                                                            'trzecia' : 'ją'
                                                                    }
                                                           }
                                    }
                    },
                   'Xb' : {
                           'koncowka' : 'ać',
                           'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'eję',
                                                                           'druga': 'ejesz',
                                                                           'trzecia': 'eje'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'ejemy',
                                                                            'druga' : 'ejecie',
                                                                            'trzecia' : 'eją'
                                                                    }
                                                           }
                                    }
                    },
                   'Xc' : {
                           'koncowka' : 'ać',
                           'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'mę',
                                                                           'druga': 'miesz',
                                                                           'trzecia': 'mie'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'miemy',
                                                                            'druga' : 'miecie',
                                                                            'trzecia' : 'mą'
                                                                    }
                                                           }
                                    }
                    },
                   'XI' : {
                           'koncowka' : 'ć',
                           'forma' : {
                                    'czas teraźniejszy' : {
                                                           'pojedyńcza' : {
                                                                           'pierwsza' : 'ę',
                                                                           'druga': 'esz',
                                                                           'trzecia': 'e'
                                                                           },
                                                           'mnoga' : {
                                                                            'pierwsza' : 'emy',
                                                                            'druga' : 'ecie',
                                                                            'trzecia' : 'ą'
                                                                    }
                                                           }
                                    }
                    },

    }


    irregular_conjugation = {
        'aspekt': {
            'niedokonane': {
                'forma': {
                    'czas przeszły': {
                        'liczba': {
                            'pojedyńcza': {
                                'osoba': {
                                    'pierwsza': {
                                        'rodzaj': {
                                            'm': 'robiłem',
                                            'ż': 'robiłam',
                                            'n': 'robiłom'
                                        }
                                    },
                                    'druga': {
                                        'rodzaj': {
                                            'm': 'robiłeś',
                                            'ż': 'robiłaś',
                                            'n': 'robiłoś'
                                        }
                                    },
                                    'trzecia': {
                                        'rodzaj': {
                                            'm': 'robił',
                                            'ż': 'robiła',
                                            'n': 'robiło'
                                        }
                                    }
                                }
                            },
                            'mnoga': {
                                'osoba': {
                                    'pierwsza': {
                                        'rodzaj': {
                                            'm': 'robiliśmy',
                                            'ż': 'robiłyśmy',
                                            'n': 'robiłyśmy'
                                        }
                                    },
                                    'druga': {
                                        'rodzaj': {
                                            'm': 'robiliście',
                                            'ż': 'robiłyście',
                                            'n': 'robiłyście'
                                        }
                                    },
                                    'trzecia': {
                                        'rodzaj': {
                                            'm': 'robili',
                                            'ż': 'robiły',
                                            'n': 'robiły'
                                        }
                                    }
                                }
                            }
                        }
                    },
                    'czas teraźniejszy': {
                        'liczba': {
                            'pojedyńcza': {
                                'osoba': {
                                    'pierwsza': 'robię',
                                    'druga': 'robisz',
                                    'trzecia': 'robi'
                                }
                            },
                            'mnoga': {
                                'osoba': {
                                    'pierwsza': 'robimy',
                                    'druga': 'robicie',
                                    'trzecia': 'robią'
                                }
                            }
                        }
                    }
                }
            },
            'dokonane': {
                'forma': {
                    'czas przesz\xc5\x82y': {
                        'liczba': {
                            'pojedy\xc5\x84cza': {
                                'osoba': {
                                    'pierwsza': {
                                        'rodzaj': {
                                            '\xc5\xbc': 'wyst\xc4\x99powa\xc5\x82am',
                                            'm': 'wyst\xc4\x99powa\xc5\x82em',
                                            'n': 'wyst\xc4\x99powa\xc5\x82om'
                                        }
                                    },
                                    'druga': {
                                        'rodzaj': {
                                            '\xc5\xbc': 'wyst\xc4\x99powa\xc5\x82a\xc5\x9b',
                                            'm': 'wyst\xc4\x99powa\xc5\x82e\xc5\x9b',
                                            'n': 'wyst\xc4\x99powa\xc5\x82o\xc5\x9b'
                                        }
                                    },
                                    'trzecia': {
                                        'rodzaj': {
                                            '\xc5\xbc': 'wyst\xc4\x99powa\xc5\x82a',
                                            'm': 'wyst\xc4\x99powa\xc5\x82',
                                            'n': 'wyst\xc4\x99powa\xc5\x82o'
                                        }
                                    }
                                }
                            },
                            'mnoga': {
                                'osoba': {
                                    'pierwsza': {
                                        'rodzaj': {
                                            '\xc5\xbc': 'wyst\xc4\x99powa\xc5\x82y\xc5\x9bmy',
                                            'm': 'wyst\xc4\x99powali\xc5\x9bmy',
                                            'n': 'wyst\xc4\x99powa\xc5\x82y\xc5\x9bmy'
                                        }
                                    },
                                    'druga': {
                                        'rodzaj': {
                                            '\xc5\xbc': 'wyst\xc4\x99powa\xc5\x82y\xc5\x9bcie',
                                            'm': 'wyst\xc4\x99powali\xc5\x9bcie',
                                            'n': 'wyst\xc4\x99powa\xc5\x82y\xc5\x9bcie'
                                        }
                                    },
                                    'trzecia': {
                                        'rodzaj': {
                                            '\xc5\xbc': 'wyst\xc4\x99powa\xc5\x82y',
                                            'm': 'wyst\xc4\x99powali',
                                            'n': 'wyst\xc4\x99powa\xc5\x82y'
                                        }
                                    }
                                }
                            }
                        }
                    },
                    'czas tera\xc5\xbaniejszy': {
                        'liczba': {
                            'pojedy\xc5\x84cza': {
                                'osoba': {
                                    'pierwsza': 'wyst\xc4\x99puj\xc4\x99',
                                    'druga': 'wyst\xc4\x99pujesz',
                                    'trzecia': 'wyst\xc4\x99puje'
                                }
                            },
                            'mnoga': {
                                'osoba': {
                                    'pierwsza': 'wyst\xc4\x99pujemy',
                                    'druga': 'wyst\xc4\x99pujecie',
                                    'trzecia': 'wyst\xc4\x99puj\xc4\x85'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    adjective_schema = {
        'exceptions': {
            'k': 'c',
            't': 'c'
        }, # end exceptions
        'y': {
            'przypadek': {
                'mianownik': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'y',
                                'ż': 'a',
                                'n': 'e'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'i',
                                'nm': 'e'
                            }
                        }
                    }
                }, # end mianownik
                'dopełniacz': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'ego',
                                'ż': 'ej',
                                'n': 'ego'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'ych',
                                'nm': 'ych'
                            }
                        }
                    }
                }, # end dopełniacz
                'celownik': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'emu',
                                'ż': 'ej',
                                'n': 'emu'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'ym',
                                'nm': 'ym'
                            }
                        }
                    }
                }, # end celownik
                'biernik': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'ego',
                                'ż': 'ą',
                                'n': 'e'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'ych',
                                'nm': 'e'
                            }
                        }
                    }
                }, # end biernik
                'narzędnik': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'ym',
                                'ż': 'ą',
                                'n': 'ym'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'ymi',
                                'nm': 'ymi'
                            }
                        }
                    }
                }, # end narzędnik
                'miejscownik': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'ym',
                                'ż': 'ej',
                                'n': 'ym'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'ych',
                                'nm': 'ych'
                            }
                        }
                    }
                }, # end miekscownik
                'wołacz': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'y',
                                'ż': 'a',
                                'n': 'e'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'i',
                                'nm': 'e'
                            }
                        }
                    }
                } # end wołacz
            } # end przypadek
        }, # end y
        'i': {
            'przypadek': {
                'mianownik': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'i',
                                'ż': 'a',
                                'n': 'ie'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'i',
                                'nm': 'ie'
                            }
                        }
                    }
                }, # end mianownik
                'dopełniacz': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'iego',
                                'ż': 'a',
                                'n': 'ie'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'ich',
                                'nm': 'ich'
                            }
                        }
                    }
                }, # end dopełniacz
                'celownik': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'iemu',
                                'ż': 'iej',
                                'n': 'iego'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'iemu',
                                'nm': 'im'
                            }
                        }
                    }
                }, # end celownik
                'biernik': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'iego',
                                'ż': 'ą',
                                'n': 'ie'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'ich',
                                'nm': 'ie'
                            }
                        }
                    }
                }, # end biernik
                'narzędnik': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'im',
                                'ż': 'ą',
                                'n': 'im'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'im',
                                'nm': 'imi'
                            }
                        }
                    }
                }, # end narzędnik
                'miejscownik': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'im',
                                'ż': 'iej',
                                'n': 'im'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'ich',
                                'nm': 'ich'
                            }
                        }
                    }
                }, # end miekscownik
                'wołacz': {
                    'liczba': {
                        'pojedyńcza': {
                            'rodzaj': {
                                'm': 'i',
                                'ż': 'a',
                                'n': 'ie'
                            }
                        },
                        'mnoga': {
                            'rodzaj': {
                                'm': 'i',
                                'nm': 'ie'
                            }
                        }
                    }
                } # end wołacz
            } # end przypadek
        } # end i
    }