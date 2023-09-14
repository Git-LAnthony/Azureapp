describe('index page', () => {
  it('visit the homepage', () => {
    cy.visit('https://resume.lamaianthony.com/');
    cy.api('https://resumefuncapp.azurewebsites.net/api/HttpTrigger?').its('status').should('equal', 200);
  })
})