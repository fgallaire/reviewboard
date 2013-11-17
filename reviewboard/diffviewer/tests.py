from django.test import TestCase
                          ("equal",  0, 6, 2, 8)])
                         [("equal",   0, 4, 0, 4),
                          ("insert",  5, 5, 5, 9),
                          ("equal",   5, 8, 9, 12)])
        print result

class DiffParserTest(unittest.TestCase):
            self.failUnless(file.origFile.startswith("%s/orig_src/" %
            self.failUnless(file.newFile.startswith("%s/new_src/" %
    def testMoveDetection(self):
        """Testing move detection"""
        differ = MyersDiffer(old.splitlines(), new.splitlines())
        r_moves = []
        i_moves = []
        opcode_generator = get_diff_opcode_generator(differ)
        for opcodes in opcode_generator:
            tag = opcodes[0]
            meta = opcodes[-1]
            if tag == 'delete':
                if 'moved' in meta:
                    r_moves.append(meta['moved'])
            elif tag == 'insert':
                if 'moved' in meta:
                    i_moves.append(meta['moved'])

        self.assertEqual(len(r_moves), 1)
        self.assertEqual(len(i_moves), 1)

        moves = [
            (15, 28),
            (16, 29),
            (17, 30),
            (18, 31),
            (19, 32)
        ]
        for i, j in moves:
            self.assertTrue(j in i_moves[0])
            self.assertTrue(i in r_moves[0])
            self.assertEqual(i_moves[0][j], i)
            self.assertEqual(r_moves[0][i], j)
                                          '<span class="hl">abc</span>')
                                          '<span class="hl">a</span>bc')
        repository = Repository.objects.get(pk=1)
        repository = Repository.objects.get(pk=1)
            'Index: README\n'
            '==========================================================='
            '========\n'
            '--- README  (revision 123)\n'
            '+++ README  (new)\n'
        repository = Repository.objects.create(
            name='Subversion SVN',
            path='file://%s' % (os.path.join(os.path.dirname(__file__),
                                             '..', 'scmtools', 'testdata',
                                             'svn_repo')),
            tool=Tool.objects.get(name='Subversion'))
            'Index: README\n'
            '==========================================================='
            '========\n'
            '--- README  (revision 123)\n'
            '+++ README  (new)\n'
        repository = Repository.objects.create(
            name='Subversion SVN',
            path='file://%s' % (os.path.join(os.path.dirname(__file__),
                                             '..', 'scmtools', 'testdata',
                                             'svn_repo')),
            tool=Tool.objects.get(name='Subversion'))
            'Index: README\n'
            '==========================================================='
            '========\n'
            '--- README  (revision 124)\n'
            '+++ README  (new)\n'
            'Index: README\n'
            '==========================================================='
            '========\n'
            '--- README  (revision 123)\n'
            '+++ README  (new)\n'
            'Index: UNUSED\n'
            '==========================================================='
            '========\n'
            '--- UNUSED  (revision 123)\n'
            '+++ UNUSED  (new)\n'
        # Note that we're using SVN here for the test just because it's
        # a bit easier to test with than Git (easier diff parsing logic
        # and revision numbers).
        repository = Repository.objects.create(
            name='Subversion SVN',
            path='file://%s' % (os.path.join(os.path.dirname(__file__),
                                             '..', 'scmtools', 'testdata',
                                             'svn_repo')),
            tool=Tool.objects.get(name='Subversion'))
        self.assertTrue(('/README', '123') in saw_file_exists)
        self.assertFalse(('/UNUSED', '123') in saw_file_exists)
                for a, b in map(None, A, B):