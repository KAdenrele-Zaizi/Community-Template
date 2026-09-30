import {
  BackLink,
  Button,
  H1,
  H2,
  Main,
  Paragraph,
  PhaseBanner,
  SectionBreak,
  TopNav,
} from 'govuk-react'
import styled from 'styled-components'

const Page = styled.div`
  max-width: 960px;
  margin: 0 auto;
  padding: 0 16px 32px;
`

const BackLinkWrap = styled.div`
  max-width: 960px;
  margin: 0 auto;
  padding: 16px 16px 0;
`

const ActionRow = styled.div`
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
`

function App() {

  return (
    <>
      <TopNav>
        <TopNav.NavLink href="#">Service name</TopNav.NavLink>
      </TopNav>
      <BackLinkWrap>
        <BackLink href="#">Back</BackLink>
      </BackLinkWrap>
      <Page>
        <PhaseBanner level="alpha">
          This is a basic sample frontend using GOV.UK styles.
        </PhaseBanner>

        <Main>
          <H1>Welcome to the sample service</H1>
          <Paragraph>
            This is a very basic page built with govuk-react and styled-components.
          </Paragraph>

          <SectionBreak visible />

          <H2>Next step</H2>
          <Paragraph>Select an action to continue.</Paragraph>

          <ActionRow>
            <Button>Start now</Button>
            <Button buttonColour="#f3f2f1" buttonTextColour="#0b0c0c">
              Save for later
            </Button>
          </ActionRow>
        </Main>
      </Page>
    </>
  )
}

export default App
