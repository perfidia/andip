#-*- coding: utf-8 -*-
'''
Created on 13-03-2013

@author: Mateusz
'''

class Schema(object):
        
    def get_word_present(self,conj_type, forma, liczba, osoba, base_word):
        print "dddd"
        new_end = conjugation[conj_type]['forma'][forma][liczba][osoba]
        print new_end
        return base_word.replace(str(conjugation[conj_type]['koncowka']), str(new_end))
    
    def get_word_past(self,conj_type, forma, liczba, rodzaj, osoba, base_word):
        new_end = conjugation[conj_type]['forma'][forma][liczba][rodzaj][osoba]
        return  base_word.replace(conjugation[conj_type]['koncowka'], new_end)
        
        
conjugation = {
               'I' : {
                      'koncowka' : 'ać',
                      'forma' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas przeszly' : {
                                                   'pojedyncza' : {
                                                                   'meski' : {
                                                                                    'pierwsza' : 'ałem',
                                                                                    'druga' : 'ałeś',
                                                                                    'trzecia' : 'ał'
                                                                              },
                                                                   'zenski' : {
                                                                                    'pierwsza' : 'ałam',
                                                                                    'druga' : 'ałaś',
                                                                                    'trzecia' : 'ała'
                                                                               },
                                                                   'nijaki' : {
                                                                                    'pierwsza' : 'ałom',
                                                                                    'druga' : 'ałoś',
                                                                                    'trzecia' : 'ało'
                                                                               }
                                                                  },
                                                   'mnoga' : {
                                                                    'meski' : {
                                                                                    'pierwsza' : 'aliśmy',
                                                                                    'druga' : 'aliście',
                                                                                    'trzecia' : 'ali'
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
                                                                               }
                                                              }
                                        }
                },
               'II' : {
                       'koncowka' : 'eć',
                       'forma' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas przeszly' : {
                                                   'pojedyncza' : {
                                                                   'meski' : {
                                                                                    'pierwsza' : 'ałem',
                                                                                    'druga' : 'ałeś',
                                                                                    'trzecia' : 'ał'
                                                                              },
                                                                   'zenski' : {
                                                                                    'pierwsza' : 'ałam',
                                                                                    'druga' : 'ałaś',
                                                                                    'trzecia' : 'ała'
                                                                               },
                                                                   'nijaki' : {
                                                                                    'pierwsza' : 'ałom',
                                                                                    'druga' : 'ałoś',
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
                                                                               }
                                                              }
                                        }
                },
               'III' : {
                        'koncowka' : 'eć',
                        'forma' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas przeszly' : {
                                                   'pojedyncza' : {
                                                                   'meski' : {
                                                                                    'pierwsza' : 'ałem',
                                                                                    'druga' : 'ałeś',
                                                                                    'trzecia' : 'ał'
                                                                              },
                                                                   'zenski' : {
                                                                                    'pierwsza' : 'ałam',
                                                                                    'druga' : 'ałaś',
                                                                                    'trzecia' : 'ała'
                                                                               },
                                                                   'nijaki' : {
                                                                                    'pierwsza' : 'ałom',
                                                                                    'druga' : 'ałoś',
                                                                                    'trzecia' : 'ało'
                                                                               }
                                                                  },
                                                   'mnoga' : {
                                                                    'meski' : {
                                                                                    'pierwsza' : 'liśmy',
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
                                                                               }
                                                              }
                                        }
                },
               'IV' : {
                       'koncowka' : 'ować',
                       'forma' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas przeszly' : {
                                                   'pojedyncza' : {
                                                                   'meski' : {
                                                                                    'pierwsza' : 'owałem',
                                                                                    'druga' : 'owałeś',
                                                                                    'trzecia' : 'ował'
                                                                              },
                                                                   'zenski' : {
                                                                                    'pierwsza' : 'owałam',
                                                                                    'druga' : 'owałaś',
                                                                                    'trzecia' : 'owała'
                                                                               },
                                                                   'nijaki' : {
                                                                                    'pierwsza' : 'owałom',
                                                                                    'druga' : 'owałoś',
                                                                                    'trzecia' : 'owało'
                                                                               }
                                                                  },
                                                   'mnoga' : {
                                                                    'meski' : {
                                                                                    'pierwsza' : 'owaliśmy',
                                                                                    'druga' : 'owaliście',
                                                                                    'trzecia' : 'owali'
                                                                              },
                                                                   'zenski' : {
                                                                                    'pierwsza' : 'owałyśmy',
                                                                                    'druga' : 'owałyście',
                                                                                    'trzecia' : 'owały'
                                                                               },
                                                                   'nijaki' : {
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
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas przeszly' : {
                                                   'pojedyncza' : {
                                                                   'meski' : {
                                                                                    'pierwsza' : 'nąłem',
                                                                                    'druga' : 'nąłeś',
                                                                                    'trzecia' : 'nął'
                                                                              },
                                                                   'zenski' : {
                                                                                    'pierwsza' : 'nęłam',
                                                                                    'druga' : 'nęłaś',
                                                                                    'trzecia' : 'nęła'
                                                                               },
                                                                   'nijaki' : {
                                                                                    'trzecia' : 'nęło'
                                                                               }
                                                                  },
                                                   'mnoga' : {
                                                                    'meski' : {
                                                                                    'pierwsza' : 'nęliśmy',
                                                                                    'druga' : 'nęliście',
                                                                                    'trzecia' : 'nęli'
                                                                              },
                                                                   'zenski' : {
                                                                                    'pierwsza' : 'nęłyśmy',
                                                                                    'druga' : 'nęłyście',
                                                                                    'trzecia' : 'nęły'
                                                                               },
                                                                   'nijaki' : {
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
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas przeszly' : {
                                                   'pojedyncza' : {
                                                                   'meski' : {
                                                                                    'pierwsza' : 'nąłem',
                                                                                    'druga' : 'nąłeś',
                                                                                    'trzecia' : 'nął'
                                                                              },
                                                                   'zenski' : {
                                                                                    'pierwsza' : 'nęłam',
                                                                                    'druga' : 'nęłaś',
                                                                                    'trzecia' : 'nęła'
                                                                               },
                                                                   'nijaki' : {
                                                                                    'trzecia' : 'nęło'
                                                                               }
                                                                  },
                                                   'mnoga' : {
                                                                    'meski' : {
                                                                                    'pierwsza' : 'nęliśmy',
                                                                                    'druga' : 'nęliście',
                                                                                    'trzecia' : 'nęli'
                                                                              },
                                                                   'zenski' : {
                                                                                    'pierwsza' : 'nęłyśmy',
                                                                                    'druga' : 'nęłyście',
                                                                                    'trzecia' : 'nęły'
                                                                               },
                                                                   'nijaki' : {
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
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'ię',
                                                                       'druga': 'isz',
                                                                       'trzecia': 'i'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'imy',
                                                                        'druga' : 'icie',
                                                                        'trzecia' : 'ią'
                                                                }
                                                       }
                                } 
                },
               'VIb' : {
                       'koncowka' : 'yć',
                       'forma' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
               'VIIa' : {
                       'koncowka' : 'eć',
                       'forma' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
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