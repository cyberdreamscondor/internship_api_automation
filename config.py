class Config:
    def __init__(self, env):
        self.base_url = {
            'local': "https://gorest.co.in"
        }[env]

        self.app_port = {
            'local': ":80"
        }[env]

        self.token = {
            "Authorization": "Bearer c8816a6b5a1ce16041be702d5b0640ed4ba524d18bd27eb35b0f09eed255845f"
        }



