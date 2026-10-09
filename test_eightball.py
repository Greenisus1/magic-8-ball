import unittest,io,contextlib
from unittest.mock import patch
import eightball as app
class Tests(unittest.TestCase):
 def test_twenty_unique(self):self.assertEqual(len(app.RESPONSES),20);self.assertEqual(len(set(app.RESPONSES)),20)
 def test_empty_no_choice(self):
  for text in ('','   ',None):
   with self.assertRaises(ValueError):app.answer(text)
 def test_chooses_only_responses(self):
  self.assertEqual(app.answer('why?',lambda values:values[0]),'It is certain')
 def test_one_answer_no_extra(self):
  out=io.StringIO()
  with contextlib.redirect_stdout(out):self.assertEqual(app.main(['--question','yes?']),0)
  self.assertIn(out.getvalue().strip(),app.RESPONSES);self.assertEqual(len(out.getvalue().splitlines()),1)
 def test_blank_then_question_quit(self):
  out=io.StringIO()
  with patch('builtins.input',side_effect=['','yes?','/quit']),contextlib.redirect_stdout(out):self.assertEqual(app.main([]),0)
  self.assertIn(out.getvalue().strip(),app.RESPONSES);self.assertEqual(len(out.getvalue().splitlines()),1)
 def test_eof(self):
  with patch('builtins.input',side_effect=EOFError):self.assertEqual(app.main([]),0)
 def test_interrupt(self):
  with patch('builtins.input',side_effect=KeyboardInterrupt):self.assertEqual(app.main([]),0)
