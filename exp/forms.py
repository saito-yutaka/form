from django import forms


class UseExpForm(forms.Form):
    # AからBに与えるポイントの選択
    use_exp = forms.IntegerField()
