def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    assert 'Hello from eazytraining' in res.get_data(as_text=True)
