#This is a document containing the complete results from the BAMS Thesaurus (fixed) basal ganglia data extraction
#The queries are below and rely on two other sets of code: One is SPARQL_BAMS_Store_Persist_Example.py and the other
#is SPARQL_BAMS_Store_Query_Example.py


#BASAL GANGLIA OF TELENCEPHALON QUERY:
	qres = g.query(
		 """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
		   SELECT ?subject ?predicate ?object
		   WHERE {
			  ?subject bamsProp:entry "Basal ganglia of telencephalon" .
			  ?subject ?predicate ?object
			}""")
	
	for r in qres.result:
		print str(r[0]), str(r[1]), str(r[2])

#RESULTS:
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/ranson-sw-1920/">Ranson, 1920</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/definition For macrodissected adult humans it includes the caudate and lentiform (putamen and globus pallidus) nuclei, amygdala, and claustrum (p. 252) and is thus not synonymous with <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>. More recently it was used in Ranson's sense by for example Clark (1951, p. 968).
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/entry Basal ganglia of telencephalon
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-of-telencephalon/ http://brancusi1.usc.edu/RDF/slug basal-ganglia-of-telencephalon

#BASAL GANGLIA QUERY:
	qres = g.query(
		 """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
		   SELECT ?subject ?predicate ?object
		   WHERE {
			  ?subject bamsProp:entry "Basal ganglia" .
			  ?subject ?predicate ?object
			}""")
	
	for r in qres.result:
		print str(r[0]), str(r[1]), str(r[2])

#RESULTS:
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/carpenter-mb-1976/">Carpenter, 1976</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://brancusi1.usc.edu/RDF/definition For macrodissected adult humans it includes the caudate and lenticular nuclei and the amygdala, and is thus not synonymous with <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; p. 496.
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://brancusi1.usc.edu/RDF/entry Basal ganglia
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-4/ http://brancusi1.usc.edu/RDF/slug basal-ganglia-4
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/ferrier-d-1876/">Ferrier, 1876</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://brancusi1.usc.edu/RDF/definition In modern terms includes for macrodissected adult monkeys and humans the <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a> and <a href="/thesaurus/definition/interbrain/"><span class="synonim_bold">interbrain (Baer, 1837)</span></a> considered together; pp. 8, 236.
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://brancusi1.usc.edu/RDF/entry Basal ganglia
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia/ http://brancusi1.usc.edu/RDF/slug basal-ganglia
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/strong-os-elwyn-a-1943/">Strong & Elwyn, 1943</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://brancusi1.usc.edu/RDF/definition Synonym for basal ganglia of telencephalon (Ranson, 1920) in macrodissected adult humans, and thus not synonymous with <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; p. 319.
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://brancusi1.usc.edu/RDF/entry Basal ganglia
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-2/ http://brancusi1.usc.edu/RDF/slug basal-ganglia-2
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/warwick-r-williams-pl-eds-1973/">Warwick & Williams, 1973</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://brancusi1.usc.edu/RDF/definition Synonym for <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; see Warwick & Williams (1973, p. 805; and Williams & Warwick, 1980, p. 864). Its use is discouraged because reference to <a href="/thesaurus/definition/ganglia/"><span class="synonim_bold">ganglia (Galen, c173)</span></a> in the <a href="/thesaurus/definition/cerebrospinal-axis/"><span class="synonim_bold">cerebrospinal axis (Meckel, 1817)</span></a> is archaic; and because "basal ganglia" today usually refers to a functional system that includes components in the <a href="/thesaurus/definition/forebrain-2/"><span class="synonim_bold">forebrain (Goette, 1873)</span></a> and <a href="/thesaurus/definition/midbrain/"><span class="synonim_bold">midbrain (Baer, 1837)</span></a>, rather than to a <a href="/thesaurus/definition/topographic-division/"><span class="synonim_bold">topographic division</span></a> of the <a href="/thesaurus/definition/endbrain/"><span class="synonim_bold">endbrain (Kuhlenbeck, 1927)</span></a>; see Anthoney (1994, pp. 106-109), DeLong & Wichmann (2007), and Federative Committee on Anatomical Terminology (1998, *A14.1.09.501).
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://brancusi1.usc.edu/RDF/entry Basal ganglia
	http://brancusi1.usc.edu/thesaurus/definition/basal-ganglia-3/ http://brancusi1.usc.edu/RDF/slug basal-ganglia-3
	
#BASAL NUCLEI QUERY:
	qres = g.query(
		 """PREFIX bamsProp: <http://brancusi1.usc.edu/RDF/>
		   SELECT ?subject ?predicate ?object
		   WHERE {
			  ?subject bamsProp:entry "Basal nuclei" .
			  ?subject ?predicate ?object
			}""")
	
	for r in qres.result:
		print str(r[0]), str(r[1]), str(r[2])

#RESULTS:
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/clark-weleg-1951/">Clark, 1951</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/definition Synonym for basal ganglia (Strong & Elwyn, 1943) in macrodissected adult humans, and thus not synonymous with <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; p. 968. Others employing this usage include Warwick & Williams (1973, p. 976; and Williams & Warwick, 1980, p. 1032), International Anatomical Nomenclature Committee (1983, p. A72).
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/entry Basal nuclei
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei/ http://brancusi1.usc.edu/RDF/slug basal-nuclei
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/workspace 0
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://www.w3.org/1999/02/22-rdf-syntax-ns#type http://brancusi1.usc.edu/RDF/thesaurus
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/reference <a target="_blank" href="/thesaurus/reference/warwick-r-williams-pl-eds-1973/">Warwick & Williams, 1973</a>
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/definition Synonym for <a href="/thesaurus/definition/cerebral-nuclei/"><span class="synonim_bold">cerebral nuclei (Swanson, 2000)</span></a>; see Warwick & Williams (1973, p. 805; and Williams & Warwick, 1980, p. 864) and Swanson (1998, p. 200).
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/entry Basal nuclei
	http://brancusi1.usc.edu/thesaurus/definition/basal-nuclei-2/ http://brancusi1.usc.edu/RDF/slug basal-nuclei-2